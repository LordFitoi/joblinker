import { PaginatedApiSchema } from "~~/utils/api";

export default defineStore('JobPostStore', {
    state() {
        return {
            objects: [],
            schema: null,
        }
    },
    actions: {
        onInit() {
            this.schema = new PaginatedApiSchema(this, API.JOBPOSTS);
            this.schema.fetch();
        }
    }
})
