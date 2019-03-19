from django.urls import path


from applications.authentication import (
    conf as authentication_conf
)
from applications.authentication import (
    api
)

urlpatterns = [
    path(
        'log-in/',
        api.GetToken.as_view(),
        name=authentication_conf.GET_TOKEN_API_URL_NAME
    )
]
