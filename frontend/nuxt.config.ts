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
            title: "Joblinker",
            htmlAttrs: { lang: 'en' },
            meta: [
                { charset: 'utf-8' },
                {
                    name: 'viewport',
                    content: 'width=device-width, initial-scale=1'
                },
                {
                    hid: 'description',
                    name: 'description',
                    content: "Discover your next career opportunity with joblinker.site! Explore a wide range of job listings and connect with employers effortlessly. Find your dream job with ease and take the next step towards a fulfilling career today"
                }
            ],
            link: [
                { rel: 'icon', type: 'image/x-icon', href: '/static/favicon.svg' }
            ],
            script: [
                {
                  src: 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9853098123219669',
                  async: true
                }
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
            dir: `./../${config.outputDir}`,
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
