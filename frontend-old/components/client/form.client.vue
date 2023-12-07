<template>
    <div class="slideout--menu" :class="{ 'active': isVisible }">
        <div class="heading">
            <h3>%{{ title }}</h3>
            <h4>%{{ subtitle }}</h4>
            <img @click="toggleVisibility()" src="~/assets/icons/x-close.svg" class="close--button">
        </div>
        <div class="content">
            <slot></slot>
        </div>
        <div class="footer">
            <button class="button--secondary" @click="onCancel()">Cancel</button>
            <button class="button--primary" @click="onSave()">Save</button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title: {
            type: String,
            required: true
        },
        subtitle: {
            type: String,
            required: true
        },
    },
    data() {
        return {
            isVisible: false,
        }
    },
    methods: {
        toggleVisibility() {
            this.isVisible = !this.isVisible;
        },
        onCancel() {
            this.toggleVisibility();
            this.$emit('cancel');
        },
        onSave() {
            this.toggleVisibility();
            this.$emit('save');
        }
    }
}
</script>
