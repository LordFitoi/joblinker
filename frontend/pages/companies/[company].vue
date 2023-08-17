<template>
    <NuxtLayout name="content">
        <div class="company--page">
            <PlaceholderCompanyDetail v-if="!store.company.schema?.isComplete" />
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
    
            <div class="container" v-if="!store.jobpost.schema?.isComplete">
                <PlaceholderJobpost v-for="_ in 5" :key="_"></PlaceholderJobpost>
            </div>
            <ClientOnly v-else>
                <div class="container no-min-height">
                    <Jobpost v-for="object in store.jobpost.objects" :key="object" :data="object"></Jobpost>
    
                    <div class="no-results" v-if="!store.jobpost.objects.length">
                        <img src="~/assets/icons/search-lg.svg">
                        No results found...
                    </div>
    
                    <div class="table--footer" v-if="paginator.totalPages > 1">
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
    </NuxtLayout>
</template>
<script>
import companyStore from '~~/stores/company.js';
import jobpostStore from '~~/stores/jobpost.js';

export default {
    setup() {
        return {
            store: {
                company: companyStore(),
                jobpost: jobpostStore()
            },
            route: useRoute()
        }
    },
    computed: {
        object() {
            return this.store.company.objects;
        },        
        paginator() {
            return this.store.jobpost.schema.paginator;
        }
    },
    mounted() {
        this.store.company.onInit(this.route.params.company);
        this.store.jobpost.onInit(this.route.params.company);

    },
    data() {
        return {
            fallback: false
        }
    }
}
</script>