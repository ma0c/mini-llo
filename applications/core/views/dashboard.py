from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from functools import reduce
from operator import or_

from applications.core import (
    conf as core_conf,
    models as core_models,
)


class Dashboard(generic.TemplateView):
    template_name = "core/dashboard/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_board_url"] = reverse_lazy(core_conf.CREATE_BOARD_URL_NAME)
        context["update_board_url_name"] = core_conf.UPDATE_BOARD_URL_NAME

        filters = [Q(is_private=False)]
        if self.request.user.is_authenticated:
            filters.append(Q(owner=self.request.user))

        context['boards'] = core_models.Board.objects.filter(reduce(or_, filters))

        context['create_idea_api_url'] = reverse_lazy(core_conf.CREATE_IDEA_API_URL_NAME)

        return context
