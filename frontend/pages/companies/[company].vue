<template>
    <div>
        <div class="placeholder" v-if="!store.schema?.isComplete">
            <div class="company-heading">
                <div class="company--logo big">.</div>
                <div class="inner">
                    <h1>.</h1>
                    <div class="cite">.</div>
                </div>
            </div>

            <h2>.</h2>
            <div class="description">.</div>
            <h2>.</h2>
        </div>
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