from django.db import models
from django.conf import settings
from core.utils import uploaded_image_filepath


class Campaign(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to=uploaded_image_filepath, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'campaigns'


