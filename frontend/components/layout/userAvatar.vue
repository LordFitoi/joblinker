<template>
    <div class="account--image">
        <img v-if="!showPlaceHolder" :src="'%{{ request.user.profile.photo.url }}'" alt="User's avatar">
        <p v-else v-text="backend.render('%{{ request.user.username|capfirst|first }}', 'N')"></p>
    </div>
</template>
<script>
export default {
    data() {
        return {
            showPlaceHolder: process.env.NODE_ENV === 'development'
        }
    }
}
</script>
