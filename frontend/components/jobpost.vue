<template>
    <a class="jobpost--item" :href="data.origin_url">
        <div class="company--logo">
            <img :src="data.logo" alt="">
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
    }
}
</script>
