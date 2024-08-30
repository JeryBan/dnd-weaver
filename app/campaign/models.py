from django.db import models
from django.conf import settings

from core.model_mixins import BaseModelMixin
from core.utils import uploaded_image_filepath


class Campaign(BaseModelMixin):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True, default='')
    image = models.ImageField(upload_to=uploaded_image_filepath, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='campaigns',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def __len__(self):
        return Campaign.objects.count()

    class Meta:
        db_table = 'campaign'
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'
        ordering = ['user', 'title']
