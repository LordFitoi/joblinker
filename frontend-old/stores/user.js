import { ApiSchema } from "~~/utils/api";

export default defineStore('UserStore', {
    state() {
        return {
            objects: [],
            schema: null,
        }
    },
    actions: {
        onInit() {
            this.schema = new ApiSchema(this, API.USERS)
            this.schema.fetch();
        }
    }
})
