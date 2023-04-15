<template>
    <div class="jobpost--item">
        <div class="company--logo"></div>
        <div>
            <h3> {{ data.title }}</h3>
            <p>{{ data.description }}</p>
            <div class="tags">
                <div class="tag badge" v-for="category in data.categories" :key="category">
                    {{ category }}
                </div>
            </div>
        </div>
    </div>
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
