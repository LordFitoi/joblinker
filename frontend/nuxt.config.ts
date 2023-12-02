import fs from 'fs'

const config = JSON.parse(fs.readFileSync('config.json', 'utf-8'));

export default defineNuxtConfig({
    ssr: true,
    modules: [
        [
            '@pinia/nuxt',
            {
                autoImports: [
                    // automatically imports `defineStore`
                    'defineStore', // import { defineStore } from 'pinia'
                    // automatically imports `defineStore` as `definePiniaStore`
                    ['defineStore', 'definePiniaStore'], // import { defineStore as definePiniaStore } from 'pinia'
                ],
            },
        ],
        'nuxt-gtag'
    ],
    app: {
        buildAssetsDir: "/static/",
        cdnURL: process.env[config.env.CDN_URL] ? process.env[config.env.CDN_URL]: '',
        head: {
            htmlAttrs: { lang: 'en' },
            meta: [
                { charset: 'utf-8' },
                {
                    name: 'viewport',
                    content: 'width=device-width, initial-scale=1'
                }
            ],
            link: [
                { rel: 'icon', type: 'image/x-icon', href: '/static/favicon.ico' }
            ]
        },
    },
    css: ['~/assets/css/styles.scss'],
    experimental: {
        payloadExtraction: false,
        componentIslands: true
    },
    nitro: {
        output: {
            dir: `./../../${config.outputDir}`,
        },
        prerender: {
            crawlLinks: false
        }
    },
    gtag: {
        id: config.env.GTAG,
        initialConsent: process.env.NODE_ENV === 'production'
    },

    generate: {
        routes: [
            '/companies/company.html'
        ]
    },
    vue: {
        compilerOptions: {
            delimiters: ['%{{', '}}']
        }
    }
})
