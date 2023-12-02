<template>
    <a class="company--item" :href="data.url">
        <div class="company--logo">
            <img v-if="data.logo && !fallback" :src="data.logo" @error="fallback=true" :alt="`${data.name} logo`">
            <img v-else src="~/assets/icons/logo.svg" class="fallback" alt="">
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
