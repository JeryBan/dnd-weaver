"""
Custom validators to use in serializers,
for better control of the data serialization
process
"""
from rest_framework import serializers


class FileExtensionValidator:
    """Validates that a file has a valid extension before saving."""

    def __call__(self, filename):

        if '.' not in filename:
            raise serializers.ValidationError('No file extension detected')

        ext = filename.split('.')[-1].lower()

        if ext not in ['png', 'jpeg', 'pjpeg', 'svg']:
            raise serializers.ValidationError('Invalid file extension')
