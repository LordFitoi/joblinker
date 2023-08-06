<template>
    <div class="page--container">
        <header>
            <NuxtLink to="/">
                <img class="logo" src="~/assets/icons/placeholder_logo.svg">
            </NuxtLink>
        </header>
        <main class="background">
            <div class="content">
                <slot></slot>
            </div>
        </main>
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