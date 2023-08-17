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

        <main class="main-container" ref="top">
            <div class="search-grid">
                <div class="search-results" v-if="!store.schema?.isComplete">
                    Loading...
                </div>
                <ClientOnly v-else>
                    <div class="search-results">
                        {{ paginator.itemsCount }} Results found
                        <span v-if="paginator.searchParams.get('search')">
                            - "{{ paginator.searchParams.get("search") }}"
                        </span>
                    </div>
                </ClientOnly>
                
                <div class="container" v-if="!store.schema?.isComplete">
                    <PlaceholderCompany v-for="_ in 10" :key="_"></PlaceholderCompany>
                </div>
                <ClientOnly v-else>
                    <div class="container">
                        <Company v-for="object in store.objects" :key="object" :data="object"></Company>
    
                        <div class="no-results" v-if="!store.objects.length">
                            <img src="~/assets/icons/search-lg.svg">
                            No results found...
                        </div>
    
                        <div class="table--footer">
                            <button class="button--secondary"
                                @click="onPrevious()"
                                :disabled="!paginator.previousPage">
                                Previous
                            </button>
                            <p class="page-counter">
                                {{ paginator.getPageText() }}
                            </p>
                            <button class="button--secondary ml-auto"
                                @click="onNext()"
                                :disabled="!paginator.nextPage">
                                Next
                            </button>
                        </div>
                    </div>
                </ClientOnly>
            </div>
        </main>
    </NuxtLayout>
</template>

<script>
import Store from '~~/stores/company.js';


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
    },
    methods: {
        onPrevious() {
            this.store.schema.previousPage();
            this.$refs.top.scrollIntoView({ behavior: 'smooth' });
        },
        onNext() {
            this.store.schema.nextPage();
            this.$refs.top.scrollIntoView({ behavior: 'smooth' });
        }
    }
}
</script>