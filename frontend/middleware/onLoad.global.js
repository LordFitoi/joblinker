export default defineNuxtRouteMiddleware((to, from) => {
    if (!process.server) {
        if (to.name === from.name && to.path.endsWith('.html')) {
            return abortNavigation()
        }
    }
})