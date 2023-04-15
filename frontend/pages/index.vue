<template>
    <main>
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
    }
}
</script>