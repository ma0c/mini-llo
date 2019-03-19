from django.contrib import admin

from applications.core import models


admin.site.register(models.Board)
admin.site.register(models.Idea)
