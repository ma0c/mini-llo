from django.urls import reverse_lazy

from rest_framework.authtoken.models import  Token

from applications.authentication import (
    conf as authentication_conf
)


def login_urls(request):
    """
    This context processor injects reversed urls to load on all views
    :param request:
    :return:
    """
    return {
        "login_url": reverse_lazy(authentication_conf.LOGIN_URL_NAME),
        "logout_url": reverse_lazy(authentication_conf.LOGOUT_URL_NAME),
    }


def authenticated_token(request):
    """
    If an user is authenticated we use restframework token to inject to the user instance a valid token
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        request.user.auth_token, _ = Token.objects.get_or_create(user=request.user)
    return dict()
