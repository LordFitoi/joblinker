<template>
    <a class="jobpost--item" :href="data.url">
        <div class="meta">
            <div class="company--logo">
                <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback" alt="">
                <img v-else :src="data.logo" @error="fallback=true" :alt="`${data.name} logo`">
            </div>
            <div class="inner">
                <span>{{ data.name }}</span>
                <cite>{{ data.website }}</cite>
            </div>
        </div>
        <p>{{ data.description }}</p>
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
