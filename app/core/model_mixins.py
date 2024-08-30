"""
Base mixins for Model classes
"""
from django.db import models


class BaseModelMixin(models.Model):
    """
    Base model info mixin
    """
    created = models.DateTimeField(
        auto_now_add=True,
        null=False,
        help_text='Creation date'
    )

    modified = models.DateTimeField(
        auto_now=True,
        null=False,
        help_text='Modified date'
    )

    is_active = models.BooleanField(
        default=True,
        null=False,
        db_index=True,
        help_text='Enabled or disabled record'
    )

    class Meta:
        abstract = True
