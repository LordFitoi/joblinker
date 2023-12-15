from django.urls import path, re_path
from . import views

urlpatterns = [
    path("signup/", views.AccountSignupView.as_view(), name="account_signup"),
    path("login/", views.AccountLoginView.as_view(), name="account_login"),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.AccountConfirmEmail.as_view(),
        name="account_confirm_email",
    ),
    re_path(
        r"^confirm-email/",
        views.AccountEmailVerificationSentView.as_view(),
        name="account_email_verification_sent",
    ),
    # path("logout/", views.logout, name="account_logout"),
]
