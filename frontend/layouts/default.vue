<template>
    <div class="page--container">
        <header>
            <img class="logo" src="~/assets/icons/placeholder_logo.svg">
            <div class="container search">
                <Searchbar ref="search" :schema="store.schema"></Searchbar>
                <button @click="$refs.search.onSearch" class="button--primary">Search</button>
            </div>
        </header>
        <slot></slot>
    </div>
</template>
<script>
import Store from '~~/stores/jobpost.js';

export default {
    setup() {
        return {
            store: Store()
        }
    },
}
</script>