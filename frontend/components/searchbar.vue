<template>
    <FormInput
        v-model="entry"
        icon="/assets/icons/search-lg.svg"
        @keydown.enter="onSearch()"
    >
    </FormInput>
</template>

<script>
export default {
    props: {
        schema: {
            type: Object,
            required: false
        }
    },
    data() {
        return {
            entry: ""
        }
    },
    methods: {
        onSearch() {
            if (this.schema) {
                this.schema.fetch(this.entry);
            }
        }
    }
}
</script>
