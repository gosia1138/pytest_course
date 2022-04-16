from django.core import mail
from django.test import TestCase


class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
        ):
            self.assertEqual(len(mail.outbox), 0)
            # Send Email
            mail.send_mail(
                subject="Test Subject",
                message="Test Message",
                from_email="testemail@gmail.com",
                recipient_list=["testemail2@gmail.com"],
                fail_silently=False,
            )
            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(mail.outbox[0].subject, "Test Subject")
