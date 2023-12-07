# Wolverine Nuxt 3 - Frontend Client

Look at the [Nuxt 3 documentation](https://nuxt.com/docs/getting-started/introduction) or checkout the [Wolverine Nuxt Wiki](https://github.com/codetigerco/wolverine-nuxt/wiki) to learn more.

## Setup

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install
```

## Django Monolith Configuration
Configure the application in `config.json`:

```json
# config.json
{
    "outputDir": "[OUTPUT_DIR]",
    "env": {
        "awsBucket": "[AWS_BUCKET_ENV_VAR]",
    }
}
```

Add this configuration in `settings.py`:

```python
NUXT_OUTPUT_DIR = "[OUTPUT_DIR]"
TEMPLATES['DIRS'] += [str(APPS_DIR / f"{NUXT_OUTPUT_DIR}/public")]
STATICFILES_DIRS += [str(APPS_DIR / f"{NUXT_OUTPUT_DIR}/public/static")]
```

Now you can run the Django server:

```bash
python manage.py runserver
```

Congratulations! You have successfully configured the Nuxt 3 monolith with Django.

## Development Server

Start the development server on http://localhost:3000

```bash
npm run dev
```

## Production

Generate application statics for production:

```bash
npm run generate
```

Locally preview production build:

```bash
npm run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
