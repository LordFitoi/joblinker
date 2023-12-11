import mailtrap as mt
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class EmailBackend(BaseEmailBackend):
    client = mt.MailtrapClient(token=settings.MAILTRAP_API_TOKEN)
    sender = mt.Address(email=settings.MAILTRAP_EMAIL, name=settings.MAILTRAP_NAME)

    def send_messages(self, email_messages):
        for email in email_messages:
            to = [mt.Address(email=email_to) for email_to in email.to]
            mail = mt.Mail(
                to=to, sender=self.sender, subject=email.subject, text=email.body
            )

            self.client.send(mail)

        return len(list(email_messages))
