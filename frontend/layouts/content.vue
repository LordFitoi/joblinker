<template>
    <div class="page--container">
        <header>
            <LayoutLogo />
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