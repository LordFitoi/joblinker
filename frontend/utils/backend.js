export const backend = {
    render(string, placeholder="Example") {
        return process.env.NODE_ENV === 'production' ? string : placeholder
    }
}