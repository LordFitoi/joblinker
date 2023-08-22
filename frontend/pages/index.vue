<template>
    <NuxtLayout name="default">
        <template #header>
            <div class="container search">
                <Searchbar 
                    ref="search" :schema="store.schema"
                    placeholder="Search job by title, description or career"
                />
                <button @click="$refs.search.onSearch" class="button--primary">Search</button>
            </div>
        </template>

        <main class="main-container">
            <h1 class="text-center">Jobposts</h1>
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

                <CardsTableJobpost />
            </div>
            <PageAd adKey="b041a54588d9c42a335ae5bb9b246885" width="728" height="90" class="horizontal margin-top" />
        </main>
    </NuxtLayout>
</template>

<script>
import Store from '~~/stores/jobpost.js';

export default {
    setup() {
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