from django.conf import settings
from django.db import models
from django.db.models.fields import validators

from campaign.models import Campaign
from core.model_mixins import BaseModelMixin
from core.utils import uploaded_image_filepath, uploaded_soundtrack_filepath


class Scenario(BaseModelMixin):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True, default='')
    order = models.IntegerField(default=0)
    lvl_requirement = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    story_mode = models.BooleanField(default=False)
    map = models.ImageField(upload_to=uploaded_image_filepath, null=True)
    soundtrack = models.FileField(upload_to=uploaded_soundtrack_filepath, null=True)
    campaign = models.ForeignKey(Campaign, related_name='scenarios',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __len__(self):
        return Scenario.objects.count()

    class Meta:
        db_table = 'scenario'
        verbose_name = 'Scenario'
        verbose_name_plural = 'Scenarios'
        ordering = ['order']


class Npc(BaseModelMixin):
    scenario = models.ForeignKey(
        Scenario,
        related_name='npcs',
        null=True,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(max_length=255, blank=True, default='')
    RACES = [
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('demi-human', 'demi-Human')
    ]
    race = models.CharField(choices=RACES, default='human', max_length=20, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='npcs',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    def __len__(self):
        return Npc.objects.count()

    class Meta:
        db_table = 'npc'
        verbose_name = 'Npc'
        verbose_name_plural = 'Npcs'


class Monster(BaseModelMixin):
    index = models.CharField(max_length=50, null=False, blank=False)
    scenario = models.ForeignKey(
        Scenario,
        related_name='monsters',
        null=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.index

    def __len__(self):
        return Monster.objects.count()

    class Meta:
        db_table = 'monster'
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'
