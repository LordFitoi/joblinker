<template>
    <div class="company--page">
        <PlaceholderCompanyDetail  v-if="!store.schema?.isComplete" />
        <ClientOnly v-else>
            <a class="company-heading" :href="object.website">
                <div class="company--logo big">
                    <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback" alt="">
                    <img v-else :src="object.logo"  @error="fallback=true" :alt="`${object.name} logo`">
                </div>
    
                <div class="inner">
                    <h1>{{ object.name }}</h1>
                    <cite>{{ object.website }}</cite>
                </div>
            </a>

            <h2>About</h2>
            <div class="description" v-html="object.description"></div>
    
            <h2>Related jobs</h2>
        </ClientOnly>

        <div class="container" >
            <PlaceholderJobpost v-for="_ in 5" :key="_"></PlaceholderJobpost>

            <div class="table--footer">
                <div class="button--secondary">Previous</div>
                <p class="page-counter">
                    Page 1 of 1
                </p>
                <div class="button--secondary ml-auto">Next</div>
            </div>
        </div>

    </div>
</template>
<script>
import Store from '~~/stores/company.js';

export default {
    setup() {
        return {
            store: Store(),
            route: useRoute()
        }
    },
    computed: {
        object() {
            return this.store.objects
        }
    },
    mounted() {
        this.store.onInit(this.route.params.company);
    },
    data() {
        return {
            fallback: false
        }
    }
}
</script>