from django.views import generic
from django.urls import reverse_lazy
from django import http
from django.contrib.auth.mixins import LoginRequiredMixin

from applications.core import (
    conf as core_conf,
    forms as core_forms,
    models as core_models,

)


class Create(LoginRequiredMixin, generic.CreateView):
    model = core_models.Board
    form_class = core_forms.Board
    template_name = "core/board/create.html"
    success_url = reverse_lazy(core_conf.MAIN_DASHBOARD_URL_NAME)

    def form_valid(self, form):
        board = form.save(commit=False)
        board.owner = self.request.user
        board.save()
        return http.HttpResponseRedirect(self.success_url)
