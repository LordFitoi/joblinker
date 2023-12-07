import { ApiSchema, PaginatedApiSchema } from "~~/utils/api";

export default defineStore('CompanyStore', {
    state() {
        return {
            objects: [],
            schema: null,
        }
    },
    actions: {
        onInit(slug="") {
            this.schema = slug
                ? new ApiSchema(this, `${API.COMPANIES}${slug}`)
                : new PaginatedApiSchema(this, API.COMPANIES);

            this.schema.fetch();
        }
    }
})
