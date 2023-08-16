<template>
    <div class="page--container">
        <header>
            <div class="links">
                <LayoutLogo />
                <NuxtLink to="/">Jobs</NuxtLink>
                <NuxtLink to="/companies">Companies</NuxtLink>
            </div>
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
import Store from '~~/stores/company.js';

export default {
    setup() {
        return {
            store: Store()
        }
    }
}
</script>