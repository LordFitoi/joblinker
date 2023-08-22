<template>
    <a class="company--item" :href="data.url">
        <div class="company--logo">
            <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback" alt="">
            <img v-else :src="data.logo" @error="fallback=true" :alt="`${data.name} logo`">
        </div>
        <div>
            <h2>%{{ data.name }}</h2>
            <p>%{{ data.description }}</p>
        </div>
    </a>
</template>

<script>
export default {
    props: {
        data: {
            type: Object,
            required: true
        },
        metaVisible: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            fallback: false
        }
    }
}
</script>
