<h1 align="center">Joblinker</h1>

## Used Technologies
- PostgreSQL (DataBase)
- Python / Django (Backend)
- Node.js / Astro (Frontend)
- Cloudflare (Proxy)
- Sentry (Debug Tool)
- Railway.app (Host)
- Mailtrap.io (SMTP)

## Backend Setup

Install `PostgreSQL` and create a database called `joblinker` with psql:
```sql
CREATE DATABASE joblinker;
```

Create a Python virtual environment and install packages:
```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Run database migrations, create admin user and then initialize dev server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Note: Backend uses the frontend statics generated with the command `npm run generate`

## Frontend Setup

To startup the frontend enter to the `/frontend/` directory and run the following commands:
```bash
npm install
npm run dev
```

Then access to Nuxt development server in [`localhost:8000`](http://localhost:8000)


## Frontend Development (Astro with Django)

The actual frontend use Astro.js to make the static pages, because astro use {} in it syntax itself, we added a preprocessor that allow you to use (()) and (%%) as an alternative to {{}} and {%%} django tags.

With this change you can fully use django template rendering in the astro pages and components.

If you made a new page, keep in mind the output name will be the path from the root page directory to the current page, but it will transform the current name file into a directory and inside of it, will be an `index.html` which is the current page file.


Example:
```
What Astro.js sees
companies/details.astro

What Django sees
companies/details/index.html
```

## Scrapper Crawling

After install the `backend` to run the scrapper just call this command:
```
python manage.py crawl
```
> Note: The scrapper will only run at 00:00 (0 GMT) on production.
