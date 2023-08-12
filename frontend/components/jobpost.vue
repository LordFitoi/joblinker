<template>
    <a class="jobpost--item" :href="data.origin_url">
        <div class="company--logo">
            <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback">
            <img v-else :src="data.logo" alt="" @error="fallback=true">
        </div>
        <div>
            <h2>{{ data.title }}</h2>
            <p>{{ data.description }}</p>
            <div class="tags">
                <div class="tag badge" v-for="category in data.categories" :key="category">
                    {{ category }}
                </div>
            </div>
        </div>
    </a>
</template>

<script>
export default {
    props: {
        data: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            fallback: false
        }
    }
}
</script>
