<template>
    <div>
        <a class="company-heading" :href="backend.render('object.website')">
            <div class="company--logo big">
                <img v-if="fallback" src="~/assets/icons/logo.svg" class="fallback" alt="">
                <img v-else :src="backend.render('object.logo.url')"  @error="fallback=true" :alt="`${backend.render('object.name')} logo`">
            </div>

            <div class="inner">
                <h1 v-text="backend.render('object.name')"></h1>
                <cite v-text="backend.render('object.website')"></cite>
            </div>
        </a>

        <h2>About <span v-text="backend.render('object.name')"></span></h2>
        <div class="description" v-text="backend.render('object.description | safe')"></div>

        <h2>Related jobs</h2>
        <div class="container">
            <PlaceholderJobpost v-for="_ in 5" :key="_"></PlaceholderJobpost>

            <div class="table--footer">
                <div class="button--secondary">Previous</div>
                <p class="page-counter">
                    Page 1 of 1
                </p>
                <div class="button--secondary ml-auto">Next</div>
            </div>
        </div>
    </div>
</template>
<script>
import '~/assets/css/pages/company.scss';


export default {
    data() {
        return {
            fallback: false
        }
    }
}
</script>