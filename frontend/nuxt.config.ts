import fs from 'fs'

const config = JSON.parse(fs.readFileSync('config.json', 'utf-8'))

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
    ],
    app: {
        buildAssetsDir: "/static/",
        cdnURL: process.env[config.env.CDN_URL] ? process.env[config.env.CDN_URL]: ''
    },
    css: ['~/assets/css/styles.scss'],
    experimental: {
        payloadExtraction: false
    },
    nitro: {
        output: {
            dir: `./../${config.outputDir}`,
        }
    },
})
