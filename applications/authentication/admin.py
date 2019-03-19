from django.contrib import admin

from applications.authentication import models

admin.site.register(models.User)
