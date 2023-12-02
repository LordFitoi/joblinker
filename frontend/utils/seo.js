export const SEO = {
    URL: 'https://joblinker.site',
    TYPE: 'website',
    TITLE: {
        GENERAL: 'Job Linker Site',
        COMPANIES: '{{ page_obj.paginator.count }} Companies - Job Linker Site',
        COMPANY: '{{ company.name }} - Job Linker Site',
        PRIVACY: 'Privacy - Job Linker Site'
    },
    DESCRIPTION: {
        GENERAL: 'Unlock your dream career with joblinker.site! Browse diverse job listings for engineers, software designers, managers & more. Your next step starts here!',
        COMPANIES: 'Discover your next career move with joblinker.site! Explore a wide range of job opportunities from top companies.',
        COMPANY: '{{ company.description | striptags | truncatechars:160 }}',
        PRIVACY: 'At JobLinker.site, your privacy is our priority. Learn about our commitment to safeguarding your personal information on our comprehensive Privacy Page.'
    },
    IMAGE: {
        GENERAL: IMAGES['/assets/images/logo.png'],
        COMPANY: `{% if company.logo %}{{ company.logo.url }}{% else %}${IMAGES['/assets/images/logo.png']}{% endif %}`,
    }

}
