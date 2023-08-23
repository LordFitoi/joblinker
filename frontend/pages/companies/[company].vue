<template>
    <NuxtLayout name="content" class="company--page">
        <PageCompanyDetails :company="$route.params.company" />
    
        <PageAd adKey="b041a54588d9c42a335ae5bb9b246885" width="728" height="90" class="horizontal margin-bottom"/>
    
        <h2>Related jobs</h2>
        <CardsTableJobpost :company="$route.params.company" />
    </NuxtLayout>
</template>
<script>
export default {
    setup() {
        if (process.server) {
            useSeoMeta({
                title: '{{ company.name }} - Joblinker Site',
                ogTitle: '{{ company.name }} - Joblinker Site',
                description: '{{ company.description | striptags | truncatechars:200 }}',
                ogDescription: '{{ company.description | striptags | truncatechars:200 }}',
                ogImage: '{{ company.logo.url }}',
                twitterCard: 'summary_large_image',
            });
        }
    }
}
</script>