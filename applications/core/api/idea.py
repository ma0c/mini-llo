from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status

from applications.core import (
    conf as core_conf,
    models as core_models,
    serializers as core_serializers,
)


class Create(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = core_serializers.Idea

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        idea = self.perform_create(serializer)
        return Response(
            {
                **serializer.data,
                **{
                    "is_approved": idea.is_approved,
                    "id": idea.id,
                    "board_id": idea.board.id
                }
            },
            status=status.HTTP_201_CREATED
        )

    def perform_create(self, serializer):
        print(serializer.validated_data)
        print(type(serializer.data))
        board = serializer.validated_data["board"]
        return core_models.Idea.objects.create(
            owner=self.request.user,
            board=board,
            text=serializer.validated_data["text"],
            is_approved=self.request.user == board.owner
        )


class List(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = core_serializers.Idea

    def get_queryset(self):
        print(core_conf.BOARD_PK_URL_KWARG)
        print(self.kwargs)
        return core_models.Idea.objects.filter(board=self.kwargs.get(core_conf.BOARD_PK_URL_KWARG, None))
