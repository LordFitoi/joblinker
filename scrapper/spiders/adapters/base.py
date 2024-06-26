import scrapy, re, math
from urllib.parse import urlparse
from django.utils.html import strip_tags
from scrapper.items import CategoryItem, CompanyItem, JobpostItem, WebOriginItem


class InvalidAdapterError(Exception):
    "Raised when the adapter validation fails"

    def __init__(self, adapter, field):
        self.message = f'{adapter} validation fails in field "{field}".'
        super().__init__(self.message)


class TextSimilarity:
    @classmethod
    def format(self, text):
        """
        Format the input text by replacing newlines and multiple spaces with single spaces.

        Args:
            text (str): The input text to be formatted.

        Returns:
            str: The formatted text.
        """

        text = re.sub("\n", " ", text)
        text = re.sub("\s+", " ", text)
        text = strip_tags(text)
        return text.strip()

    @classmethod
    def get_subwords(self, word):
        """Returns the subwords the word"""
        return set([word[i : i + 3] for i in range(len(word) - 2)])

    @classmethod
    def get_similarity(self, text_a, text_b):
        subwords_a = self.get_subwords(text_a)
        subwords_b = self.get_subwords(text_b)

        return len(subwords_a) / len(subwords_a.union(subwords_b))


class ValidationMixin:
    is_active = True
    min_similarity_bias = 0.7

    def validate_company(self, response, company):
        """
        Validate company data by comparing crawled data with provided data.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.
            company (CompanyItem): The company data to be validated.

        Returns:
            bool: True if company data is valid, False otherwise.
        """

        if not self.is_active:
            return False

        crawled_company = self.get_company(response)

        self.is_active = all(
            [
                company.name == crawled_company["name"],
                company.origin_url == crawled_company["origin_url"],
                self.format_and_striptags(company.description)
                == self.format_and_striptags(crawled_company["description"]),
            ]
        )

    def validate_jobpost(self, response, jobpost):
        """
        Validate job post data by comparing crawled data with provided data.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.
            jobpost (JobpostItem): The job post data to be validated.

        Returns:
            bool: True if job post data is valid, False otherwise.
        """

        if not self.is_active:
            return False

        crawled_jobpost = self.get_jobpost(response)

        fields_to_validate = ["title", "origin_url", "description"]

        for field in fields_to_validate:
            local_object = self.format_and_striptags(getattr(jobpost, field))
            scrapped_object = self.format_and_striptags(crawled_jobpost[field])

            if (
                TextSimilarity.get_similarity(local_object, scrapped_object)
                < self.min_similarity_bias
            ):
                self.is_active = False
                raise InvalidAdapterError(self, field)

    def validate(self, objects):
        """
        Validate job post and company data by sending requests to validate the associated URLs.

        Args:
            objects (dict): A dictionary containing 'jobpost' and 'company' objects.

        Yields:
            scrapy.http.Request: Requests to validate job post and company data.
        """
        yield scrapy.Request(
            objects["jobpost"].origin_url,
            callback=self.validate_jobpost,
            cb_kwargs=dict(jobpost=objects["jobpost"]),
        )

        yield scrapy.Request(
            objects["company"].origin_url,
            callback=self.validate_company,
            cb_kwargs=dict(company=objects["company"]),
        )


class BaseAdapter(ValidationMixin):
    """
    Base class for adapters to scrape job-related data from websites.
    """

    selectors = {}
    pages = []
    root_page = ""

    def format(self, text):
        """
        Format the input text by replacing newlines and multiple spaces with single spaces.

        Args:
            text (str): The input text to be formatted.

        Returns:
            str: The formatted text.
        """

        text = re.sub("\n", " ", text)
        text = re.sub("\s+", " ", text)
        return text.strip()

    def format_and_striptags(self, text):
        """
        Apply formatting to the input text using `format` method and strip any HTML tags.

        Args:
            text (str): The input text to be formatted.

        Returns:
            str: The formatted and stripped text.
        """

        text = strip_tags(text)
        return self.format(text)

    def get_nextpage(self, response):
        """
        Extract the URL for the next page from the response and return a request to follow it.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.

        Returns:
            scrapy.http.Request or None: A request to follow the next page link, or None if
            no next page is found.
        """
        if self.pages:
            next_page = self.pages.pop()
            return response.follow(next_page, callback=self.parse)

    def get_categories(self, response, selector):
        labels = set(response.xpath(selector).getall())
        return [CategoryItem(name=label) for label in labels]

    def get_logo_url(self, response, selector):
        """
        Extract the logo URL using the provided selector from the response.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.
            selector (str): The selector used to locate the logo URL.

        Returns:
            str: The extracted logo URL.
        """

        return (
            f"https://{urlparse(response.url).hostname}{response.xpath(selector).get()}"
        )

    def get_weborigin(self, response):
        """
        Extract web origin data from the response URL and return as a WebOriginItem instance.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.

        Returns:
            WebOriginItem: An instance of WebOriginItem containing web origin data.
        """

        return WebOriginItem(
            **{
                "name": urlparse(response.url).hostname,
                "website": f"https://{urlparse(response.url).hostname}",
            }
        )

    def get_company(self, response):
        """
        Extract company data from the response using selectors and return as a CompanyItem instance.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.

        Returns:
            CompanyItem: An instance of CompanyItem containing company data.
        """

        selectors = self.selectors["company"]

        return CompanyItem(
            **{
                "name": response.xpath(selectors["name"]).get().strip(),
                "website": f'https://{urlparse(response.xpath(selectors["website"]).get()).netloc}',
                "description": self.format(
                    response.xpath(selectors["description"]).get()
                ),
                "origin_url": response.url,
            }
        )

    def parse_company(self, response, jobpost, weborigin):
        """
        Parse company information from the response and yield a dictionary containing relevant data.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.
            jobpost (JobpostItem): The job post data associated with the company.
            weborigin (WebOriginItem): The web origin data associated with the company.

        Yields:
            dict: A dictionary containing parsed company, job post, and web origin data.
        """

        selectors = self.selectors["company"]

        yield {
            "logo_url": self.get_logo_url(response, selectors["logo_url"]),
            "company": self.get_company(response),
            "jobpost": jobpost,
            "weborigin": weborigin,
        }

    def get_jobpost(self, response):
        """
        Extract job post data from the response using selectors and return as a JobpostItem
        instance.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.

        Returns:
            JobpostItem: An instance of JobpostItem containing job post data.
        """

        selectors = self.selectors["jobpost"]

        return JobpostItem(
            **{
                "title": response.xpath(selectors["title"]).get().strip(),
                "description": self.format(
                    response.xpath(selectors["description"]).get()
                ),
                "origin_url": response.url,
                "categories": self.get_categories(response, selectors["categories"]),
            }
        )

    def parse_jobpost(self, response, weborigin):
        """
        Parse job post information from the response and yield requests to parse associated company
        information.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.
            weborigin (WebOriginItem): The web origin data associated with the job post.

        Yields:
            scrapy.http.Request: Requests to parse company information.
        """

        yield response.follow(
            response.xpath(self.selectors["jobpost"]["company_link"]).get(),
            callback=self.parse_company,
            cb_kwargs=dict(jobpost=self.get_jobpost(response), weborigin=weborigin),
        )

    def parse(self, response):
        """
        Parse the response to extract job card links, yield requests to parse job post information,
        and yield a request for the next page.

        Args:
            response (scrapy.http.Response): The response containing the webpage content.

        Yields:
            scrapy.http.Request: Requests to parse job post information and for the next page.
        """

        jobcards = response.xpath(self.selectors["link"]).getall()

        for link in jobcards:
            yield response.follow(
                link,
                callback=self.parse_jobpost,
                cb_kwargs=dict(weborigin=self.get_weborigin(response)),
            )

        yield self.get_nextpage(response)

    def __str__(self):
        return f"<{self.__class__.__name__}>"
