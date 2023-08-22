<template>
    <div class="page--container">
        <header id="header">
            <div class="links">
                <LayoutLogo />
                <NuxtLink to="/">Jobs</NuxtLink>
                <NuxtLink to="/companies">Companies</NuxtLink>
            </div>
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