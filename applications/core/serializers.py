from rest_framework import serializers

from applications.core import (
    models as core_models
)


class Board(serializers.ModelSerializer):
    class Meta:
        model = core_models.Board
        fields = (
            'id',
            'name'
        )


class Idea(serializers.ModelSerializer):
    class Meta:
        model = core_models.Idea
        fields = (
            'board',
            'text'
        )


