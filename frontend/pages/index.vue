<template>
    <main ref="top">
        <div class="search-grid">
            <ClientOnly>
                <div class="search-results">
                    {{ paginator.itemsCount }} Results found
                    <span v-if="paginator.searchParams.get('search')">
                        - "{{ paginator.searchParams.get("search") }}"
                    </span>
                </div>
            </ClientOnly>
            <div class="container" v-if="!store.schema?.isComplete">
                <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost>
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