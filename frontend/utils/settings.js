export const SETTINGS = {
    PAGINATION_MAX_ITEMS_COUNT: 100,
    CKEDITOR_CONFIG: {
        height: 154,
        removePlugins: [
            'elementspath',
            'exportpdf'
        ],
        resize_enabled: false,
        toolbar: [
           [
                'Bold',
                'Italic',
                'Link',
                'NumberedList',
                'BulletedList'
            ]
        ],
        contentsCss: [
            "STATIC_PATH" + "css/editor.css"
        ]
    },
}

export const API = {
    BASE: '/api/',
    USER: 'users/me/',
    USERS: 'users/',
};
