<template>
    <NuxtLayout name="default">
        <template #header>
            <div class="container search">
                <Searchbar
                    ref="search" :schema="store.schema"
                    placeholder="Search company by title, description or career"
                />
                <button @click="$refs.search.onSearch" class="button--primary">Search</button>
            </div>
        </template>

        <main class="main-container">
            <h1 class="text-center">Companies</h1>
            <div class="search-grid">
                <div class="search-results" v-if="!store.schema?.isComplete">
                    Loading...
                </div>
                <ClientOnly v-else>
                    <div class="search-results">
                        %{{ paginator.itemsCount }} Results found
                        <span v-if="paginator.searchParams.get('search')">
                            - "%{{ paginator.searchParams.get("search") }}"
                        </span>
                    </div>
                </ClientOnly>

                <CardsTableCompany />
            </div>
            <!-- <PageAd adKey="b041a54588d9c42a335ae5bb9b246885" width="728" height="90" class="horizontal margin-top" /> -->
        </main>
    </NuxtLayout>
</template>

<script>
import Store from '~~/stores/company.js';


export default {
    setup() {
        useServerSeoMeta({
            title: SEO.TITLE.COMPANIES,
            description: SEO.DESCRIPTION.COMPANIES,
            ogType: SEO.TYPE,
            ogUrl: SEO.URL,
            ogTitle: SEO.TITLE.COMPANIES,
            ogDescription: SEO.DESCRIPTION.COMPANIES,
            ogImage: SEO.IMAGE.GENERAL,
            twitterUrl: SEO.URL,
            twitterTitle: SEO.TITLE.COMPANIES,
            twitterDescription: SEO.DESCRIPTION.COMPANIES,
            twitterImage: SEO.IMAGE.GENERAL
        });
        return {
            store: Store()
        }
    },
    mounted() {
        this.store.onInit();
    },
    computed: {
        paginator() {
            return this.store.schema.paginator;
        }
    }
}
</script>
