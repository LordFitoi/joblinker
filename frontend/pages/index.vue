<template>
    <main>
        <div class="container search">
            <FormInput
                type="text"
                icon="/assets/icons/search-lg.svg">
            </FormInput>
            <button class="button--primary">Search</button>
        </div>
        <div class="search-grid">
            <div class="container">
                <!-- <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost> -->
                <Jobpost v-for="object in store.objects" :key="object" :data="object"></Jobpost>
            </div>
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