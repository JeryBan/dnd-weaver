"""
Custom authentication backend
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        user, created = User.objects.get_or_create(username=username)

        if created:
            user.set_password(password)
            user.save()

        if user.check_password(password):
            return user
        return None
