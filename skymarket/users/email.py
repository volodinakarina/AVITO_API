from djoser import utils
from djoser.conf import settings
from templated_mail.mail import BaseEmailMessage


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        pass
