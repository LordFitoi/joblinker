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
            <PageAd adKey="b041a54588d9c42a335ae5bb9b246885" width="728" height="90" class="horizontal margin-top" />
        </main>
    </NuxtLayout>
</template>

<script>
import Store from '~~/stores/company.js';


export default {
    setup() {
        useServerSeoMeta({
            title: '{{ page_obj.paginator.count }} Companies - Joblinker Site',
            ogTitle: '{{ page_obj.paginator.count }} Companies - Joblinker Site',
            description: 'Discover your next career move with joblinker.site! Explore a wide range of job opportunities from top companies. Our job board connects talented professionals with their dream roles. Find the perfect job that matches your skills and aspirations today.',
            ogDescription: 'Discover your next career move with joblinker.site! Explore a wide range of job opportunities from top companies. Our job board connects talented professionals with their dream roles. Find the perfect job that matches your skills and aspirations today.',
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