<template>
    <div class="flex flex-col gap-6" id="timeoff-request-app">
        <div class="header space-between--container items-center">
            <h1>Payments</h1>
            <LayoutSearchbar></LayoutSearchbar>
        </div>
        <hr class="divider">

        <div class="space-between--container">
            <div class="details--block">
                <h3>Payment history</h3>
            </div>
            <div class="buttons--container">
                <button class="button--secondary">
                    Download All
                </button>
                <button class="button--primary" @click="$refs.form.container.toggleVisibility()">
                    Payment
                </button>
            </div>
        </div>
        <ClientTable
            class="columns-time-off-request"
            v-slot="props"
            :store="store"
            :columns="[
                ['Transfer', 'payment_date'],
                ['Amount', 'amount'],
                ['Date', 'payment_date'],
                ['Status', 'status']
            ]"
        >
            <div><p class="title">{{ format.date(props.object.payment_date) }}</p></div>
            <div><p>{{ format.amount(props.object.amount) }}</p></div>
            <div><p>{{ format.date(props.object.payment_date) }}</p></div>
            <div><ClientBadge :state="props.object.status"></ClientBadge></div>
        </ClientTable>
        <ExampleForm ref="form" :user="user" :store="store"></ExampleForm>
    </div>
</template>
<script>
import store from '~/stores/example';

export default {
    setup() {
        return {
            store: store(),
            user: {}
        }
    },
    mounted() {
        this.store.onInit();
    }
}

</script>
