<template>
    <a class="jobpost--item" :href="backend.addUrlReference(data.origin_url)">
        <div v-if="metaVisible" class="meta">
            <div class="company--logo">
                <img v-if="data.company.logo && !fallback" :src="data.company.logo" @error="fallback=true" :alt="`${data.company.name} logo`">
                <img v-else src="~/assets/icons/logo.svg" class="fallback" alt="">
            </div>
            <div class="inner">
                <span>%{{ data.company.name }}</span>
                <cite>%{{ data.origin_url }}</cite>
            </div>
        </div>
        <div>
            <h2>%{{ data.title }}</h2>
            <p>%{{ data.description }}</p>
            <div class="tags" v-if="data.categories.length">
                <div class="tag badge" v-for="category in data.categories" :key="category">
                    %{{ category }}
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
