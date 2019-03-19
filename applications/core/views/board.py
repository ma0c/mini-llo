from django.views import generic
from django.urls import reverse_lazy
from django import http
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.utils import NestedObjects

from applications.core import (
    conf as core_conf,
    forms as core_forms,
    mixins as core_mixins,
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


class Update(core_mixins.BoardOwnership, generic.UpdateView):
    model = core_models.Board
    form_class = core_forms.Board
    template_name = "core/board/update.html"
    success_url = reverse_lazy(core_conf.MAIN_DASHBOARD_URL_NAME)
    pk_url_kwarg = core_conf.BOARD_PK_URL_KWARG

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_board_url'] = reverse_lazy(
            core_conf.DELETE_BOARD_URL_NAME,
            kwargs={
                core_conf.BOARD_PK_URL_KWARG: self.get_object().id
            }
        )
        return context


class Delete(core_mixins.BoardOwnership, generic.DeleteView):
    model = core_models.Board
    template_name = "core/board/delete.html"
    context_object_name = "board"
    pk_url_kwarg = core_conf.BOARD_PK_URL_KWARG
    success_url = reverse_lazy(core_conf.MAIN_DASHBOARD_URL_NAME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()

        return context

    def post(self, request, *args, **kwargs):
        super(Delete, self).post(request, *args, **kwargs)

        return http.HttpResponseRedirect(reverse_lazy(core_conf.MAIN_DASHBOARD_URL_NAME))
