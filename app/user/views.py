"""
Views for handling user API.
"""
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer
from rest_framework import (
    viewsets,
    authentication,
    permissions
)
from django.contrib.auth import get_user_model
from user.serializers import AuthTokenSerializer, UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = (JSONRenderer,)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]

    queryset = get_user_model().objects.all()

    def get_permissions(self):
        """Allow unauthorized users to create account."""
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


class PlayerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    queryset = get_user_model().objects.filter(is_player=True)
