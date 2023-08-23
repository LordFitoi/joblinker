export const format = {
    date(date, options={ year: 'numeric', month: 'short', day: 'numeric'}) {
        date = typeof date == 'object' ? date : new Date(date);
        return date.toLocaleDateString('default', options);
    },
    time(date, options={ hour: '2-digit', minute: '2-digit' }) {
        date = typeof date == 'object' ? date : new Date(date);
        return date.toLocaleTimeString('default', options);
    },
    month(month) {
        return month.toLocaleString('default', {
            month: 'long',
            year: 'numeric'
        });
    },
    amount(amount) {
        return `USD $${amount}`;
    }
}
