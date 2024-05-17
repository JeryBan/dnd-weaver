from django.db import models
from django.conf import settings
from django.db.models.fields import validators
from django.db.models.signals import pre_save
from django.dispatch import receiver
from campaign.models import Campaign
from core.utils import uploaded_image_filepath, uploaded_soundtrack_filepath


class BaseCreature:
    """Base class for scenario creatures"""
    name = models.CharField(max_length=255)
    lvl = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    background = models.TextField(max_length=255, null=True)
    image = models.ImageField(upload_to=uploaded_image_filepath, null=True)

    class Meta:
        abstract = True


class Scenario(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='scenarios',
                                 on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    order = models.IntegerField(default=0)
    lvl_requirement = models.IntegerField(default=1, validators=[validators.MinValueValidator(1)])
    map = models.ImageField(upload_to=uploaded_image_filepath, null=True)
    soundtrack = models.FileField(upload_to=uploaded_soundtrack_filepath, null=True)
    story_mode = models.BooleanField(default=False)
    combat_mode = models.BooleanField(default=False)
    npcs = models.ManyToManyField('Npc', related_name='scenarios', blank=True)
    monsters = models.ManyToManyField('Monster', related_name='scenarios', blank=True)

    def __str__(self):
        return self.title

    def __len__(self):
        return Scenario.objects.count()

    class Meta:
        db_table = 'scenarios'


@receiver(pre_save, sender=Scenario)
def ensure_mutual_exclusivity(sender, instance, **kwargs):
    """Ensure that a scenario can be either story or combat mode."""
    if instance.story_mode:
        instance.combat_mode = False
    elif instance.combat_mode:
        instance.story_mode = False


class Npc(models.Model, BaseCreature):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    RACES = [
        ('human', 'Human'),
        ('elf', 'Elf'),
        ('demi-human', 'demi-Human')
    ]
    race = models.CharField(choices=RACES, default='human', max_length=20)

    def __str__(self):
        return self.name

    def __len__(self):
        return Npc.objects.count()

    class Meta:
        db_table = 'npcs'


class Monster(models.Model, BaseCreature):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    RACES = [
        ('animal', 'Animal'),
        ('humanoid', 'Humanoid')
    ]
    race = models.CharField(choices=RACES, default='humanoid', max_length=20)
    gear = models.TextField(max_length=255, null=True)
    actions = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def __len__(self):
        return Monster.objects.count()

    class Meta:
        db_table = 'monsters'


