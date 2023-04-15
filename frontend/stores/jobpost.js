import { PaginatedApiSchema } from "~~/utils/api";

export default defineStore('ExampleStore', {
    state() {
        return {
            objects: [],
            schema: null,
        }
    },
    actions: {
        onInit() {
            this.schema = new PaginatedApiSchema(this, 'api/jobposts/');
            this.schema.fetch();
        }
    }
})
