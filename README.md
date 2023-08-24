<h1 align="center">Joblinker</h1>

## Used Technologies
- PostgreSQL
- Python / Django
- Node.js / Nuxt
- Cloudflare Proxy
- Sentry
- Railway.app

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

To access the backend server enter here [`localhost:8000`](http://localhost:8000)

> Note: Backend uses the frontend statics generated with the command `npm run generate`

## Frontend Setup

To startup the frontend enter to the `/frontend/` directory and run the following commands:
```bash
npm install
npm run dev
```

Then access to Nuxt development server in [`localhost:3000`](http://localhost:3000)

## Scrapper Crawling

After install the `backend` to run the scrapper just call this command:
```
python manage.py crawl
```
> Note: The scrapper will only run at 00:00 (0 GMT) on production.
