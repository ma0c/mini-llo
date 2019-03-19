from django.views import generic
from django.urls import reverse_lazy

from applications.core import (
    conf as core_conf,
    models as core_models,
)


class Dashboard(generic.TemplateView):
    template_name = "core/dashboard/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["create_board_url"] = reverse_lazy(core_conf.CREATE_BOARD_URL_NAME)

        context['boards'] = core_models.Board.objects.all()

        return context
