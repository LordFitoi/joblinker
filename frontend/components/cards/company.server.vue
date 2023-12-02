<template>
    <a class="company--item" href="/companies/{{ object.slug }}">
        <div class="company--logo">
            {% if object.logo %}
                <img :src="'{{ object.logo.url }}'" alt="{{ object.name }} logo">
            {% else %}
                <img src="~/assets/images/logo.png" class="fallback"  alt="">
            {% endif %}
        </div>
        <div>
            <h2>{{ object.name }}</h2>
            <p>{{ object.description | striptags | truncatechars:200 }}</p>
        </div>
    </a>
</template>
