from django.core.mail import EmailMultiAlternatives
from django.template import loader

from common.constants import ApplicationMessages
from drive_ai import settings


class Email:
    """Email class takes the properties and send the email and handles exceptions
    It can send single mail or bulk mails"""

    def __init__(
        self,
        subject,
        template_file,
        template_params,
        to_email,
        from_email=settings.FROM_EMAIL,
        files=None,
    ):
        """Initialize the subject, template_file, and params, from email, to email"""

        self.subject = subject
        self.template_file = template_file
        self.template_params = template_params
        self.to_email = [to_email] if isinstance(to_email, str) else to_email
        self.from_email = from_email
        self.files = files

        if self.files is None:
            self.files = []

    def send(self):
        """This method uses EmailMultiAlternatives which is core package for using mail backend"""

        html_message = loader.render_to_string(self.template_file, self.template_params)
        # set the email subject, body, from, to, reply_to, bcc, headers for the email
        mail = EmailMultiAlternatives(
            self.subject, html_message, self.from_email, self.to_email, headers={}
        )
        mail.attach_alternative(html_message, "text/html")
        # attach all the files first
        for file in self.files:
            mail.attach_file(file)
        return mail.send(settings.FAIL_SILENTLY)


class ResetPasswordMail(Email):
    """
    A utility class to handle sending password reset emails to users.

    This class inherits from the base `Email` class and adds specific functionality for
    formatting and sending password reset emails to users who have requested it.
    The email contains a verification code which is essential for the password reset process.
    """

    def __init__(self, params):
        """
        Initialize ResetPasswordMail with necessary parameters.

        This constructor sets up the email attributes based on the provided parameters.
        It then calls the base Email class to handle the actual sending of the email.
        """
        self.subject = ApplicationMessages.RESET_EMAIL_SUBJECT
        self.template_file = "user/reset_email.html"
        self.template_params = {
            "user": params.get("user"),
            "verification_code": params.get("verification_code")
        }

        self.to_email = params.get("email")
        self.from_email = settings.FROM_EMAIL
        super().__init__(
            self.subject, self.template_file, self.template_params, self.to_email
        )
        obj = Email
        obj.send(self)
        del obj
        
class SignupOTP(Email):
    """
    A utility class to handle sending password reset emails to users.

    This class inherits from the base `Email` class and adds specific functionality for
    formatting and sending password reset emails to users who have requested it.
    The email contains a verification code which is essential for the password reset process.
    """

    def __init__(self, params):
        """
        Initialize ResetPasswordMail with necessary parameters.

        This constructor sets up the email attributes based on the provided parameters.
        It then calls the base Email class to handle the actual sending of the email.
        """
        print('SignupOTP called')
        self.subject = ApplicationMessages.RESET_EMAIL_SUBJECT
        self.template_file = "user/reset_email.html"
        self.template_params = {
            "verification_code": params.get("verification_code")
        }

        self.to_email = params.get("email")
        self.from_email = settings.FROM_EMAIL
        super().__init__(
            self.subject, self.template_file, self.template_params, self.to_email
        )
        obj = Email
        obj.send(self)
        del obj
