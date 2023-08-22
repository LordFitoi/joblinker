<template>
    <LayoutAside>
        <h2 id="company-name" v-text="backend.render('%{{ view.kwargs.company|capfirst }}', 'Codetiger')"></h2>
        <LayoutSearchbar></LayoutSearchbar>
        <ClientOnly>
            <div class="options--container">
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/home-line.svg"> Home
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/graduation-hat-02.svg"> Development Plan
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/heart.svg"> Benefits
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/user-01.svg"> Personal Details
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/laptop-02.svg"> Assigned Equipment
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/reverse-left.svg"> Refunds
                </NuxtLink>
                <NuxtLink class="disabled">
                    <img width="24" height="24" src="~/assets/icons/plane.svg"> Time Off
                </NuxtLink>
                <NuxtLink :to="getPath('payments')" :class="getClass('payments')">
                    <img width="24" height="24" src="~/assets/icons/credit-card-plus.svg"> Payments
                </NuxtLink>
            </div>
        </ClientOnly>
    </LayoutAside>
</template>

<script>
export default {
    methods: {
        getClass(path) {
            return {
                'active': this.$route.name == path
            }
        },
        getPath(path) {
            return `/company/${path}`
        }
    }
}
</script>
