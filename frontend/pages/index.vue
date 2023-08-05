<template>
    <main ref="top">
        <div class="container search">
            <Searchbar ref="search" :schema="store.schema"></Searchbar>
            <button @click="$refs.search.onSearch" class="button--primary">Search</button>
        </div>
        <div class="search-grid">
            <div class="container" v-if="!store.schema?.isComplete">
                <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost>
            </div>
            <ClientOnly v-else>
                <div class="container">
                    <Jobpost v-for="object in store.objects" :key="object" :data="object"></Jobpost>

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
            
            <aside class="container"></aside>
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