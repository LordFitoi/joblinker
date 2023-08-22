<template>
    <div class="table--container">
        <div class="table--head">
            <div v-for="column in columns" :key="column" class="clickable" @click="onSort(store.objects, column[1])">
                %{{ column[0] }} <img :class="{'rotate-180': lastSortDirection=='asc' && lastSortProperty==column[1]}" src="~/assets/icons/arrow.svg">
            </div>
        </div>
        <div class="table--body" v-for="object in store.objects" :key="object">
            <slot :object="object"></slot>
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
</template>

<script>
export default {
    props: {
        store: {
            type: Object,
            required: true
        },
        columns: {
            type: Array,
            required: true
        }
    },
    computed: {
        paginator() {
            return this.store.schema.paginator;
        }
    },
    data() {
        return {
            lastSortProperty: null,
            lastSortDirection: null,
        }
    },
    methods: {
        onSort(objects, property=null) {
            objects.sort((a, b) => a[property] > b[property] ? 1 : -1);

            if (this.lastSortProperty == property) {
                if (this.lastSortDirection === "asc") {
                    objects.reverse();
                    this.lastSortDirection = "desc"
                } else {
                    this.lastSortDirection = "asc";
                }
            } else {
                this.lastSortProperty = property;
                this.lastSortDirection = "asc";
            }
        },
        onPrevious() {
            this.paginator.toPreviousPage(() => {
                this.store.fetch();
            });
        },
        onNext() {
            this.paginator.toNextPage(() => {
                this.store.fetch();
            });
        }
    }
}
</script>
