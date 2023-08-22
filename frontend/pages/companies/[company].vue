<template>
    <NuxtLayout name="content" class="company--page">
        <PageCompanyDetails :company="route.params.company" />
    
        <PageAd adKey="b041a54588d9c42a335ae5bb9b246885" width="728" height="90" class="horizontal margin-bottom"/>
    
        <h2>Related jobs</h2>
        <CardsTableJobpost :company="route.params.company" />
    </NuxtLayout>
</template>
<script>
export default {
    meta: {
        script: [{ src: "~/assets/ads.js" }],
    },
    setup() {
        return {
            route: useRoute()
        }
    },
}
</script>