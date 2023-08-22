<template>
    <div>
        <div class="container">
            {% for object in object_list %}
                <CardsJobpost />
            {% endfor %}

            <div class="table--footer">
                {% if page_obj.has_previous %}
                    <NuxtLink class="button--secondary" to="?page={{ page_obj.previous_page_number }}">
                        Previous
                    </NuxtLink>
                {% else %}
                    <button class="button--secondary" disabled>
                        Previous
                    </button>
                {% endif %}

                <p class="page-counter">
                    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
                </p>

                {% if page_obj.has_next %}
                    <NuxtLink class="button--secondary ml-auto" to="?page={{ page_obj.next_page_number }}">
                        Next
                    </NuxtLink>
                {% else %}
                    <button class="button--secondary ml-auto" disabled>
                        Previous
                    </button>
                {% endif %}
            </div>
        </div>
    </div>
</template>
