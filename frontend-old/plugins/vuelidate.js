import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default defineNuxtPlugin(() => {
    return {
        provide: {
            useVuelidate: useVuelidate,
            validators: { required }

        }
    }
})
