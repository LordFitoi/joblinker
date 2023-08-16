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
                    <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost>
    
                    <div class="table--footer">
                        <div class="button--secondary">Previous</div>
                        <p class="page-counter">
                            Page 1 of 1
                        </p>
                        <div class="button--secondary ml-auto">Next</div>
                    </div>
                </div>
                <ClientOnly v-else>
                    <div class="container">
                        <Jobpost v-for="object in store.objects" :key="object" :data="object"></Jobpost>
    
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
import Store from '~~/stores/jobpost.js';

export default {
    setup() {
        definePageMeta({ layout: false });

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