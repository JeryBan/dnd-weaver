"""
Models for user.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)


class CustomUserManager(BaseUserManager):
    """User Manager to handle new users."""

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('username is required.')

        if extra_fields.get('is_dm'):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_player', False)

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('username is required.')

        extra_fields.setdefault('is_dm', True)

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_dm = models.BooleanField(default=False)
    is_player = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
