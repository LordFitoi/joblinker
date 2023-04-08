<template>
    <div class="input--container">
        <ClientOnly>
            {{ label }}
            <label tabindex="-1" class="input">
                <img v-if="icon" :src="getImage()">
                <input
                    :type="type"
                    :placeholder="placeholder"
                    :value="modelValue"
                    @change="onInput($event)"
                    @blur="onBlur()">
            </label>
            <p class="error--label" v-if="validator.$error">
                {{ validator.$errors[0].$message }}
            </p>

            <template #fallback>
                {{ label }}
                <label tabindex="-1" class="input">
                    <img v-if="icon" :src="getImage()">
                    <input :type="type" :placeholder="placeholder">
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
        type: {
            type: String,
            default: 'text'
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
    methods: {
        onBlur() {
            if (this.validator.hasOwnProperty('$touch')) {
                this.validator.$touch();
            }
        },
        getImage() {
            return ICONS[this.icon];
        },
        onInput(event) {
            this.$emit('update:modelValue', event.target.value);
        }
    }
}
</script>