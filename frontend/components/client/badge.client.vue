<template>
    <div class="badge" :class="current.class">
        <img :src="icon">
        <span>{{ state }}</span>
    </div>
</template>
<script>
export default {
    props: {
        state: {
            type: String,
            required: true
        },
    },
    setup() {
        return {
            states: {
                Approved: {
                    class: 'success',
                    icon: '/assets/icons/check_03.svg'
                },
                Rejected: {
                    class: 'cancel',
                    icon: '/assets/icons/x-close.svg'
                },
                Pending: {
                    class: 'pending',
                    icon: '/assets/icons/clock.svg'
                }
            }
        }
    },
    computed: {
        current() {
            return this.states[this.state];
        },
        icon() {
            return ICONS[this.current.icon];
        }
    }
}
</script>
