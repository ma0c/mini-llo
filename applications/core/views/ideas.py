from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import http

from applications.core import (
    conf as core_conf,
    mixins as core_mixins,
    models as core_models,
)


class PendingIdeas(LoginRequiredMixin, generic.ListView):
    template_name = "core/ideas/pending_ideas.html"
    context_object_name = "ideas"

    def get_queryset(self):
        return core_models.Idea.objects.filter(
            board__owner=self.request.user,
            is_approved=False
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approve_or_delete_idea_url_name'] = core_conf.APPROVE_OR_REMOVE_IDEA_URL_NAME
        print(context)
        return context


class ApproveOrRemoveIdea(core_mixins.IdeaOwnership, generic.UpdateView):
    template_name = "core/ideas/approve_or_delete.html"
    model = core_models.Idea
    fields = []
    context_object_name = "idea"
    pk_url_kwarg = core_conf.IDEA_PK_URL_KWARG

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_idea_url'] = reverse_lazy(
            core_conf.REMOVE_IDEA_URL_NAME,
            kwargs={
                core_conf.IDEA_PK_URL_KWARG: self.get_object().pk
            })
        return context

    def form_valid(self, form):
        idea = self.get_object()
        idea.is_approved = True
        idea.save()
        return http.HttpResponseRedirect(reverse_lazy(core_conf.APPROVE_IDEAS_LIST_URL_NAME))


class RemoveIdea(core_mixins.IdeaOwnership, generic.DeleteView):
    model = core_models.Idea
    success_url = reverse_lazy(core_conf.APPROVE_IDEAS_LIST_URL_NAME)
    pk_url_kwarg = core_conf.IDEA_PK_URL_KWARG
