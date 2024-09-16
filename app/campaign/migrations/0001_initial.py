# Generated by Django 3.2.4 on 2024-09-16 18:37

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Creation date')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Modified date')),
                ('is_active', models.BooleanField(db_index=True, default=True, help_text='Enabled or disabled record')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='', max_length=255)),
                ('image', models.ImageField(null=True, upload_to=core.utils.uploaded_image_filepath)),
            ],
            options={
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
                'db_table': 'campaign',
                'ordering': ['user', 'title'],
            },
        ),
    ]