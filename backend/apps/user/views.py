from allauth.account.views import SignupView, LoginView, ConfirmEmailView


class AccountSignupView(SignupView):
    template_name = "accounts/signup/index.html"


account_signup = AccountSignupView.as_view()


class AccountLoginView(LoginView):
    template_name = "accounts/login/index.html"


account_login = AccountLoginView.as_view()


class AccountConfirmEmail(ConfirmEmailView):
    pass
