export const backend = {
    render(string) {
        return `{{ ${string} }}`;
    },
    addUrlReference(url) {
        const domain = window.location.hostname;

        return process.env.NODE_ENV === 'production'
            ? `${url}/?ref=${domain}&source=${domain}`
            : url;
    }
}
