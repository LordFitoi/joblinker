from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from allauth.account.views import (
    SignupView,
    LoginView,
    ConfirmEmailView,
    EmailVerificationSentView,
)
from .models import Profile


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    slug_field = "user__username"
    slug_url_kwarg = "username"
    template_name = "users/index.html"


class AccountSignupView(SignupView):
    template_name = "accounts/signup/index.html"


class AccountLoginView(LoginView):
    template_name = "accounts/login/index.html"


class AccountConfirmEmail(ConfirmEmailView):
    template_name = "accounts/confirm-email/index.html"


class AccountEmailVerificationSentView(EmailVerificationSentView):
    template_name = "accounts/verification-sent/index.html"
