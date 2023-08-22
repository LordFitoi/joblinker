<template>
    <div>
        <div class="container" v-if="!store.schema?.isComplete">
            <CardsJobpostPlaceholder v-for="_ in 10" :key="_"></CardsJobpostPlaceholder>
        </div>
        <div class="container" v-else>
            <CardsJobpost v-for="object in store.objects" :key="object" :data="object"></CardsJobpost>

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
                    %{{ paginator.getPageText() }}
                </p>
                <button class="button--secondary ml-auto"
                    @click="onNext()"
                    :disabled="!paginator.nextPage">
                    Next
                </button>
            </div>
        </div>
    </div>
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
            document.querySelector("#header").scrollIntoView({ behavior: 'smooth' });
        },
        onNext() {
            this.store.schema.nextPage();
            document.querySelector("#header").scrollIntoView({ behavior: 'smooth' });
        }
    }
}
</script>
