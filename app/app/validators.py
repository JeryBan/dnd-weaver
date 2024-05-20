"""
Custom validators to use in serializers,
for better control of the data serialization
process
"""
from rest_framework import serializers


class FileExtentionValidator:
    """Validates that a file has a valid extention before saving."""

    def __call__(self, filename):

        if '.' not in filename:
            raise serializers.ValidationError('No file extention detected')

        ext = filename.split('.')[-1].lower()

        if ext not in ['png', 'jpeg', 'pjpeg', 'svg']:
            raise serializers.ValidationError('Invalid file extention')
