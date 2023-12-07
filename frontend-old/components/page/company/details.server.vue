<template>
    <div>
        <a class="company-heading" href="{{ company.website }}?ref=www.joblinker.site&source=www.joblinker.site">
            <div class="company--logo big">
                {% if company.logo %}
                    <img :src="'{{ company.logo.url }}'" alt="{{ company.name }} logo">
                {% else %}
                    <img src="~/assets/images/logo.png" class="fallback"  alt="">
                {% endif %}
            </div>

            <div class="inner">
                <h1>{{ company.name }}</h1>
                <cite>{{ company.website }}</cite>
            </div>
        </a>

        <h2>About</h2>
        <div class="description">
            {{ company.description | safe }}
        </div>
    </div>
</template>
