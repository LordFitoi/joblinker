<template>
    <main>
        <div class="container search">
            <FormInput
                type="text"
                icon="/assets/icons/search-lg.svg">
            </FormInput>
            <button class="button--primary">Search</button>
        </div>
        <div class="search-grid">
            <div class="container">
                <PlaceholderJobpost v-for="_ in 10" :key="_"></PlaceholderJobpost>  
            </div>
            <aside class="container"></aside>
        </div>
    </main>
</template>