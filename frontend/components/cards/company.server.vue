<template>
    <a class="company--item" href="/companies/{{ object.slug }}">
        <div class="company--logo">
            <img :src="'{{ object.logo.url }}'" alt="{{ object.name }} logo">
        </div>
        <div>
            <h2>{{ object.name }}</h2>
            <p>{{ object.description | striptags | truncatechars:200 }}</p>
        </div>
    </a>
</template>