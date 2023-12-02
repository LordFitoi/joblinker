<template>
    <a class="jobpost--item" href="{{ object.origin_url }}?ref=www.joblinker.site&source=www.joblinker.site">
        <div class="meta">
            <div class="company--logo">
                {% if object.company.logo %}
                    <img :src="'{{ object.company.logo.url }}'" alt="{{ object.company.name }} logo">
                {% else %}
                    <img src="~/assets/images/logo.png" class="fallback"  alt="{{ object.name }} logo">
                {% endif %}
            </div>
            <div class="inner">
                <span>{{ object.company.name }}</span>
                <cite>{{ object.origin_url }}</cite>
            </div>
        </div>
        <div>
            <h2>{{ object.title }}</h2>
            <p>{{ object.description | striptags | truncatechars:200 }}</p>

            {% if object.categories %}
            <div class="tags">
                {% for category in object.categories.all %}
                <div class="tag badge">
                    {{ category.name }}
                </div>
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </a>
</template>
