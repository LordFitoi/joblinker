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
        useServerSeoMeta({
            title: SEO.TITLE.COMPANY,
            description: SEO.DESCRIPTION.COMPANY,
            ogType: SEO.TYPE,
            ogUrl: SEO.URL,
            ogTitle: SEO.TITLE.COMPANY,
            ogDescription: SEO.DESCRIPTION.COMPANY,
            ogImage: SEO.IMAGE.COMPANY,
            twitterUrl: SEO.URL,
            twitterTitle: SEO.TITLE.COMPANY,
            twitterDescription: SEO.DESCRIPTION.COMPANY,
            twitterImage: SEO.IMAGE.COMPANY
        });
    }
}
</script>
