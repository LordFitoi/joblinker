<template>
    <aside>
        <div class="aside-options--container">
            <slot></slot>
        </div>
        <div class="aside-settings--container">
            <div class="options--container">
                <slot name="extra-options"></slot>
                <a class="disabled" href="">
                    <img width="24" height="24" src="~/assets/icons/life-buoy-01.svg"> Support
                </a>
                <a class="disabled" href="">
                    <img width="24" height="24" src="~/assets/icons/settings-01.svg"> Settings
                </a>
            </div>
            <form class="account--container" method="post" >
                <input type="hidden" name="csrfmiddlewaretoken" value="%{{ csrf_token }}">
                <LayoutUserAvatar></LayoutUserAvatar>
                <div>
                    <h3 v-text="backend.render('%{{ request.user.get_full_name|default:request.user.username }}', 'Nahum Santana')"></h3>
                    <h4 v-text="backend.render('%{{ request.user.email }}', 'nahum@codetiger.co')"></h4>
                </div>
                <button type="submit">
                    <img width="20" height="20" src="~/assets/icons/log-out-01.svg">
                </button>
            </form>
        </div>
    </aside>
</template>
