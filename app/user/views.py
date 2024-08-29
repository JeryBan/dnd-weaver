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
    permission_classes = (permissions.AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = get_user_model().objects.all()


class PlayerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    queryset = get_user_model().objects.filter(is_dm=False)
