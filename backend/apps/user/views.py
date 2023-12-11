from allauth.account.views import SignupView, LoginView, ConfirmEmailView, EmailVerificationSentView


class AccountSignupView(SignupView):
    template_name = "accounts/signup/index.html"


class AccountLoginView(LoginView):
    template_name = "accounts/login/index.html"


class AccountConfirmEmail(ConfirmEmailView):
    template_name = "accounts/confirm-email/index.html"


class AccountEmailVerificationSentView(EmailVerificationSentView):
    template_name = "accounts/verification-sent/index.html"
