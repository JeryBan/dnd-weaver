# Generated by Django 3.2.4 on 2024-05-09 13:40

import core.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('race', models.CharField(choices=[('animal', 'Animal'), ('humanoid', 'Humanoid')], default='humanoid', max_length=20)),
                ('lvl', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('gear', models.TextField(max_length=255, null=True)),
                ('actions', models.TextField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to=core.utils.uploaded_image_filepath)),
            ],
        ),
        migrations.CreateModel(
            name='Npc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('race', models.CharField(choices=[('human', 'Human'), ('elf', 'Elf'), ('demi-human', 'demi-Human')], default='human', max_length=20)),
                ('lvl', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('background', models.TextField(max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to=core.utils.uploaded_image_filepath)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255, null=True)),
                ('order', models.IntegerField(default=0)),
                ('lvl_requirement', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('map', models.ImageField(null=True, upload_to=core.utils.uploaded_image_filepath)),
                ('soundtrack', models.FileField(null=True, upload_to=core.utils.uploaded_soundtrack_filepath)),
                ('story_mode', models.BooleanField(default=True)),
                ('combat_mode', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to='campaign.campaign')),
                ('monsters', models.ManyToManyField(blank=True, related_name='scenarios', to='scenario.Monster')),
                ('npcs', models.ManyToManyField(blank=True, related_name='scenarios', to='scenario.Npc')),
            ],
        ),
    ]
