from django.db import models
from backend.apps.utils import AbstractBaseModel


class WebsiteOrigin(AbstractBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    json_scrap_origin = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(AbstractBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Location(AbstractBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(AbstractBaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    origin = models.ForeignKey(WebsiteOrigin, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

class JobPost(AbstractBaseModel):
    class JobType(models.TextChoices):
        PART_TIME = "Part Time"
        FULL_TIME = "Full Time"
        CONTRACT = "Contract"
        INTERNSHIP = "Internship"

    class Status(models.TextChoices):
        ACTIVE = "Active"
        INACTIVED = "Inactive"
        DELETED = "Deleted"
        EXPIRED = "Expired"

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    origin = models.ForeignKey(WebsiteOrigin, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    origin_url = models.URLField(blank=True, null=True)
    application_url = models.URLField(blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.FULL_TIME)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    currency = models.CharField(max_length=10, default="USD")
    start_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    end_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_remote = models.BooleanField(default=False)
    release_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.company.name}" 