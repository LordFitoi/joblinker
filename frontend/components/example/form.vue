<template>
    <ClientForm ref="container" title="Add payment" subtitle="Log a payment to a member" @save="onSave()">
        <FormInput
            label="Amount"
            :validator="v$.fields.amount"
            v-model="fields.amount"
            type="number"
            icon="/assets/icons/currency-dollar.svg"
        />
        <FormInput
            label="Payment date"
            :validator="v$.fields.payment_date"
            type="date"
            v-model="fields.payment_date"
            icon="/assets/icons/calendar.svg"
        />
        <FormSelect
            label="Status"
            placeholder="Select a status"
            :validator="v$.fields.status"
            v-model="fields.status"
            icon="/assets/icons/activity.svg"
        >
            <option value="Pending">Pending</option>
            <option value="Rejected">Rejected</option>
            <option value="Approved">Approved</option>
        </FormSelect>
    </ClientForm>
</template>

<script>
import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default {
    props: {
        store: {
            type: Object,
            required: true
        },
    },
    setup() {
        return {
            v$: useVuelidate(),
        }
    },
    data() {
        return {
            
            fields: {
                amount: null,
                payment_date: null,
                user: null,
                status: null,
            }
        }
    },
    computed: {
        container() {
            return this.$refs.container;
        }
    },
    validations () {
        return {
            fields: {
                amount: { required },
                payment_date: { required },
                status: { required }
            }
        }
    },
    methods: {
        async onSave() {
            if (await this.v$.$validate()) {
                alert('FORM SUBMITTED');
            } else {
                this.container.toggleVisibility();
            }
        }
    }
}
</script>
