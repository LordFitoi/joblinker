<template>
    <div class="page--container">
        <header>
            <LayoutLogo />
            <div class="container search">
                <Searchbar ref="search" :schema="store.schema"></Searchbar>
                <button @click="$refs.search.onSearch" class="button--primary">Search</button>
            </div>
        </header>
        <slot></slot>
        <LayoutFooter />
    </div>
</template>
<script>
import Store from '~~/stores/jobpost.js';

export default {
    setup() {
        return {
            store: Store()
        }
    }
}
</script>