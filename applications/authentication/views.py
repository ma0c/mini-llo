from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import (
    views as auth_views
)


from applications.authentication import (
    conf as authentication_conf,
    forms as authentication_forms
)


class SignUp(generic.CreateView):
    form_class = authentication_forms.SignUp
    template_name = "authentication/signup.html"
    success_url = reverse_lazy(authentication_conf.LOGIN_URL_NAME)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = reverse_lazy(authentication_conf.LOGIN_URL_NAME)
        return context


class LogIn(auth_views.LoginView):
    template_name = "authentication/login.html"
    form_class = authentication_forms.LogIn

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup_url'] = reverse_lazy(authentication_conf.SIGNUP_URL_NAME)
        return context


class LogOut(auth_views.LogoutView):
    pass
