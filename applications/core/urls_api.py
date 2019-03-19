from django.urls import path


from applications.core import (
    conf as core_conf
)
from applications.core.api import (
    idea,
    board
)

urlpatterns = [
    path(
        'boards/',
        board.List.as_view(),
        name=core_conf.LIST_BOARDS_API_URL_NAME
    ),
    path(
        'create-idea/',
        idea.Create.as_view(),
        name=core_conf.CREATE_IDEA_API_URL_NAME
    ),
    path(
        f'board/<int:{core_conf.BOARD_PK_URL_KWARG}>/ideas',
        idea.List.as_view(),
        name=core_conf.LIST_IDEAS_BY_BOARD_API_URL_NAME
    ),
]
