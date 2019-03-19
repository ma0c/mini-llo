from django.urls import path


from applications.core import (
    conf as core_conf
)
from applications.core.views import (
    board,
    dashboard
)

urlpatterns = [
    path(
        'create-board',
        board.Create.as_view(),
        name=core_conf.CREATE_BOARD_URL_NAME
    ),
    path(
        '',
        dashboard.Dashboard.as_view(),
        name=core_conf.MAIN_DASHBOARD_URL_NAME
    )
]