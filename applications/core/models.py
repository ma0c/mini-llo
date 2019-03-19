

from django.db import models

from applications.authentication import (
    models as authentication_models
)


class Board(models.Model):
    owner = models.ForeignKey(authentication_models.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    is_private = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Idea(models.Model):
    owner = models.ForeignKey(authentication_models.User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    text = models.TextField()
    is_approved = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.board}, {self.text}"
