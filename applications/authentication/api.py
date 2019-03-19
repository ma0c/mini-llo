from rest_framework import parsers, renderers

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken import models


class GetToken(APIView):
    """
    Migrated from DRF to avoid problems with same label app conflicts
    """
    throttle_classes = ()
    permission_classes = (
        AllowAny,
    )
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (
        renderers.JSONRenderer,
    )
    serializer_class = AuthTokenSerializer

    def dispatch(self, request, *args, **kwargs):
        print("On this obtain token")
        return super(GetToken, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = models.Token.objects.get_or_create(user=user)
        print(user)

        return Response(
            {
                'token': token.key,
            }
        )
