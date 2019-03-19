from django.urls import reverse_lazy

from applications.core import (
    conf as core_conf
)


def core_menu(request):
    return {
        "approve_ideas_url": reverse_lazy(core_conf.APPROVE_IDEAS_LIST_URL_NAME)
    }
