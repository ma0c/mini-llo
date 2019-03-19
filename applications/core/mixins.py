from django.contrib.auth.mixins import LoginRequiredMixin
from django import http

from django.template.loader import get_template

from applications.core import (
    conf as core_conf,
    models as core_models
)


class BoardOwnership(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().handle_no_permission()
        try:
            if request.user != core_models.Board.objects.get(pk=kwargs.get(core_conf.BOARD_PK_URL_KWARG, None)).owner:
                return http.HttpResponseForbidden(get_template("403.html").render())
        except core_models.Idea.DoesNotExist:
            return http.HttpResponseNotFound(get_template("404.html").render())

        return super().dispatch(request, *args, **kwargs)


class IdeaOwnership(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().handle_no_permission()
        try:
            if request.user != core_models.Idea.objects.get(pk=kwargs.get(core_conf.IDEA_PK_URL_KWARG, None)).board.owner:
                return http.HttpResponseForbidden(get_template("403.html").render())
        except core_models.Idea.DoesNotExist:
            return http.HttpResponseNotFound(get_template("404.html").render())

        return super().dispatch(request, *args, **kwargs)


