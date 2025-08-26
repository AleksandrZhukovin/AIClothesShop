from django.urls import reverse_lazy

from server.settings.components.common import INSTALLED_APPS, MIDDLEWARE


INSTALLED_APPS += [
    "allauth",
    "allauth.account",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]

ACCOUNT_EMAIL_VERIFICATION = "optional"
LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGOUT_REDIRECT_URL = reverse_lazy("index")
LOGIN_URL = reverse_lazy("account_login")

SOCIALACCOUNT_PROVIDERS = {}
