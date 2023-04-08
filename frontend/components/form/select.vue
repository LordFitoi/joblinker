<template>
    <div class="input--container">
        <ClientOnly>
            {{ label }}
            <label ref="input" tabindex="-1" class="input dropdown">
                <img v-if="icon" :src="getImage()">
                <p v-if="value">{{ value.innerText }}</p>
                <p class="placeholder" v-else>{{ placeholder }}</p>
                <img class="arrow" src="~/assets/icons/chevron-down.svg">
                <div class="dropdown--container" @click="onInput($event)">
                    <slot></slot>
                </div>
            </label>
            <p class="error--label" v-if="validator.$error">
                {{ validator.$errors[0].$message }}
            </p>
            
            <template #fallback>
                {{ label }}
                <label ref="input" tabindex="-1" class="input dropdown">
                    <img v-if="icon" :src="getImage()">
                    <p class="placeholder">{{ placeholder }}</p>
                    <img class="arrow" src="~/assets/icons/chevron-down.svg">
                </label>
            </template>
        </ClientOnly>
    </div>
</template>

<script>
export default {
    emits: ['update:modelValue'],
    props: {
        validator: {
            type: Object,
            default: {
                $error: false,
                $errors: []
            }
        },
        label: {
            type: String,
            default: ''
        },
        placeholder: {
            type: String,
            default: 'Write here...'
        },
        icon: {
            type: String,
            default: ''
        },
        modelValue: ''
    },
    data() {
        return {
            value: ''
        }
    },
    methods: {
        getImage() {
            return ICONS[this.icon];
        },
        setOption(event) {
            if (this.value) this.value.classList.remove('active');

            this.value = event.target;
            this.value.classList.add('active');
            this.$refs.input.blur();
        },
        onInput(event) {
            if (event.target.tagName == 'OPTION') {
                this.$emit('update:modelValue', event.target.value);
                this.setOption(event);
            }
        }
    }
}
</script>