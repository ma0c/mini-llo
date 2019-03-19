from django.urls import path


from applications.authentication import (
    views as authentication_views,
    conf as authentication_conf
)

urlpatterns = [
    path(
        'sign-up',
        authentication_views.SignUp.as_view(),
        name=authentication_conf.SIGNUP_URL_NAME
    ),
    path(
        'log-in',
        authentication_views.LogIn.as_view(),
        name=authentication_conf.LOGIN_URL_NAME
    ),
    path(
        'log-out',
        authentication_views.LogOut.as_view(),
        name=authentication_conf.LOGOUT_URL_NAME
    )
]
