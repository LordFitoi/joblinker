import { PaginatedApiSchema } from "~~/utils/api";

export default defineStore('ExampleStore', {
    state() {
        return {
            objects: [
                {
                    payment_date: "2021-01-01",
                    amount: 100,
                    status: 'Approved'
                },
                {
                    payment_date: "2023-01-01",
                    amount: 1000,
                    status: 'Pending'
                },
                {
                    payment_date: "2021-01-01",
                    amount: 200,
                    status: 'Approved'
                },
                {
                    payment_date: "2022-12-11",
                    amount: 30,
                    status: 'Rejected'
                }
            ],
            schema: null,
        }
    },
    actions: {
        onInit() {
            this.schema = new PaginatedApiSchema(this, 'api/example/');
        }
    }
})
