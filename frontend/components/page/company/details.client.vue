<template>
    <div>
        <PageCompanyDetailsPlaceholder v-if="!store.schema?.isComplete" />
        <div v-else>
            <a class="company-heading" :href="backend.addUrlReference(object.website)">
                <div class="company--logo big">
                    <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback" alt="">
                    <img v-else :src="object.logo" @error="fallback=true" :alt="`${object.name} logo`">
                </div>

                <div class="inner">
                    <h1>%{{ object.name }}</h1>
                    <cite>%{{ object.website }}</cite>
                </div>
            </a>

            <h2>About</h2>
            <div class="description" v-html="object.description"></div>
        </div>
    </div>
</template>
<script>
import store from '~~/stores/company.js';

export default {
    props: {
        company: {
            type: String,
            default: ""
        }
    },
    setup() {
        return {
            store: store()
        }
    },
    computed: {
        object() {
            return this.store.objects;
        }
    },
    mounted() {
        this.store.onInit(this.company);
    },
    data() {
        return {
            fallback: false
        }
    }
}
</script>