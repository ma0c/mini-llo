from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    identification_number = models.CharField(max_length=12)
    picture = models.FileField(null=True, blank=True)
