import { PaginatedApiSchema } from "~~/utils/api";

export default defineStore('JobPostStore', {
    state() {
        return {
            objects: [],
            schema: null,
        }
    },
    actions: {
        onInit(companySlug=null) {
            this.schema = new PaginatedApiSchema(this, API.JOBPOSTS);

            if (companySlug) {
                this.schema.paginator.searchParams.set("company", companySlug);
            }
            this.schema.fetch();
        }
    }
})
