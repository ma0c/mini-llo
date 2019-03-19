from django.urls import path


from applications.core import (
    conf as core_conf
)
from applications.core.views import (
    board,
    dashboard,
    ideas
)

urlpatterns = [
    path(
        'create-board',
        board.Create.as_view(),
        name=core_conf.CREATE_BOARD_URL_NAME
    ),
    path(
        f'update-board/<int:{core_conf.BOARD_PK_URL_KWARG}>',
        board.Update.as_view(),
        name=core_conf.UPDATE_BOARD_URL_NAME
    ),
    path(
        f'delete-board/<int:{core_conf.BOARD_PK_URL_KWARG}>',
        board.Delete.as_view(),
        name=core_conf.DELETE_BOARD_URL_NAME
    ),
    path(
        '',
        dashboard.Dashboard.as_view(),
        name=core_conf.MAIN_DASHBOARD_URL_NAME
    ),
    path(
        'pending-ideas',
        ideas.PendingIdeas.as_view(),
        name=core_conf.APPROVE_IDEAS_LIST_URL_NAME
    ),
    path(
        f'approve-or-remove-idea/<int:{core_conf.IDEA_PK_URL_KWARG}>',
        ideas.ApproveOrRemoveIdea.as_view(),
        name=core_conf.APPROVE_OR_REMOVE_IDEA_URL_NAME
    ),
    path(
        f'remove-idea/<int:{core_conf.IDEA_PK_URL_KWARG}>',
        ideas.RemoveIdea.as_view(),
        name=core_conf.REMOVE_IDEA_URL_NAME
    )
]