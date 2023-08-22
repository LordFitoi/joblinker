<template>
    <a class="jobpost--item" href="{{ object.origin_url }}?ref=www.joblinker.site&source=www.joblinker.site">
        <div class="meta">
            <div class="company--logo">
                <img :src="'{{ object.company.logo.url }}'" alt="{{ object.company.name }} logo">
            </div>
            <div class="inner">
                <span>{{ object.company.name }}</span>
                <cite>{{ object.origin_url }}</cite>
            </div>
        </div>
        <div>
            <h2>{{ object.title }}</h2>
            <p>{{ object.description | striptags | truncatechars:200 }}</p>
        </div>
    </a>
</template>
