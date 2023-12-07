<template>
    <iframe class="ad" :src="src" :height="height" :width="width" frameborder="0" scrolling="no"></iframe>
</template>
<script>
export default {
    props: {
        adKey:  {
            type: String,
            required: true
        },
		height: {
            type: String,
            required: true
        },
		width: {
            type: String,
            required: true
        }
    },
    computed: {
        src() {
            return process.env.NODE_ENV === 'development' ? null
                : `//wizardunstablecommissioner.com/watchnew?key=${this.adKey}`
        }
    }
}
</script>
