"""
Helper functions
"""
import os
import uuid
from django.conf import settings


def uploaded_image_filepath(instance, filename):
    """Generates the file path for the uploaded image."""
    extension = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{extension}'
    model_name = instance.__class__.__name__.lower()

    return os.path.join(settings.IMAGE_DIR, model_name, filename)


def uploaded_soundtrack_filepath(instance, filename):
    """Generates the file path for the uploaded soundtrack."""
    extension = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{extension}'
    model_name = instance.__class__.__name__.lower()

    return os.path.join(settings.SOUNDTRACK_DIR, model_name, filename)
