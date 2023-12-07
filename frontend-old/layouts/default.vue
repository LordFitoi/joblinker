<template>
    <div class="page--container">
        <header id="header">
            <div class="links">
                <LayoutLogo />
                <NuxtLink to="/">Jobs</NuxtLink>
                <NuxtLink to="/companies">Companies</NuxtLink>
            </div>
            <slot name="header"></slot>
        </header>
        <slot></slot>
        <LayoutFooter />
    </div>
</template>
