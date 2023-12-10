from django.urls import path, re_path
from allauth.account import views as auth
from . import views

urlpatterns = [
    path("signup/", view=views.account_signup, name="account_signup"),
    path("login/", view=views.account_login, name="account_login"),
    # path("logout/", views.logout, name="account_logout"),
]
