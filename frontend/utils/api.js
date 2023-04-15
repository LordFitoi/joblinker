import axios from 'axios';

export function Client(contentType='application/json') {
    const CSRF_TOKEN =  document.getElementsByName("csrfmiddlewaretoken")[0];

    return axios.create({
        baseURL: API.BASE,
        headers: {
            'Content-Type': contentType,
            'X-CSRFToken':  CSRF_TOKEN ? CSRF_TOKEN.value : null,
        }
    })
}

export  class Paginator {
    constructor() {
        this.totalPages = 1;
        this.nextPage = null;
        this.previousPage = null;
        this.results = [];
        this.searchParams = new URLSearchParams();
    }
    setQueryParams(url, searchEntry=null) {
        searchEntry
            ? this.searchParams.set("search", searchEntry)
            : this.searchParams.delete("search");

        return `${url}?${this.searchParams.toString()}`;
    }
    toNextPage(callback=()=>{}) {
        if (this.nextPage) {
            this.searchParams.set("page", this.nextPage);
            callback();
        }
    }
    toPreviousPage(callback=()=>{}) {
        if (this.previousPage) {
            this.searchParams.set("page", this.previousPage);
            callback();
        }
    }
    extractPageNumber(url) {
        if (url) {
            let urlObject = new URL(url);
            return urlObject.searchParams.get("page") || 1;
        }

        return null;

    }
    processResponse(response) {
        this.results = response.data.results;
        this.nextPage = this.extractPageNumber(response.data.next);
        this.previousPage = this.extractPageNumber(response.data.previous);
        this.totalPages = Math.max(response.data.count / SETTINGS.PAGINATION_MAX_ITEMS_COUNT, 1);
    }
    getPageText() {
            let page = 1;

            if (this.nextPage) {
                page = this.nextPage - 1;
            }
            else if (this.previousPage) {
                page = this.previousPage + 1;
            }

            return `Page ${page} of ${this.totalPages}`
    }
}

export class ApiSchema {
    constructor(store, path, contentType='application/json') {
        this.client = Client(contentType);
        this.store = store;
        this.path = path;
        this.isComplete = false;

        if (SETTINGS.DEV_MODE) {
            this.path = `http://127.0.0.1:8000/${this.path}`;
        }
    }
    setQueryParams(queryParams={}) {
        let params = new URLSearchParams(queryParams);
        return `${this.path}?${params.toString()}`;
    }
    callStoreMethod(methodName, params) {
        if (this.store[methodName]) {
            return this.store[methodName](params);
        }
    }
    fetch(queryParams={}) {
        let path = this.setQueryParams(queryParams);
        this.isComplete = false;

        return this.client.get(path).then(response => {
            this.isComplete = true;
            this.store.objects = response.data;
            this.callStoreMethod('onFetch', response);
        })
    }
    create(data, queryParams={}) {
        let path = this.setQueryParams(queryParams);
        
        return this.client.post(path, data).then(response => {
            this.store.objects.push(response.data);
            this.callStoreMethod('onCreate', response);
        });
    }
    // TODO: Add Update and Delete Functionality
    // put(path, data) {
    //     return this.client.put(path, data);
    // }

    // delete(path) {
    //     return this.client.delete(path);
    // }
}

export class PaginatedApiSchema extends ApiSchema {
    constructor(store, path, contentType='application/json') {
        super(store, path, contentType);
        this.paginator = new Paginator();
    }

    fetch(searchEntry=null) {
        let path = this.paginator.setQueryParams(this.path, searchEntry);
        this.isComplete = false;

        return this.client.get(path).then(response => {
            this.isComplete = true;
            console.log(this.isComplete);
            this.paginator.processResponse(response);
            this.store.objects = this.paginator.results;
            this.callStoreMethod('onFetch', response);
        })
    }
}
