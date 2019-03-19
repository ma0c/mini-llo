from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status

from applications.core import (
    models as core_models,
    serializers as core_serializers,
)


class List(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = core_serializers.Board

    def get_queryset(self):
        return core_models.Board.objects.filter(owner=self.request.user)
