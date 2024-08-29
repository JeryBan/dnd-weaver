"""
Serializers for handling campaign data.
"""
from rest_framework import serializers, validators
from campaign.models import Campaign
from core.validators import FileExtensionValidator


class CampaignListSerializer(serializers.ModelSerializer):
    image = serializers.FileField(validators=[FileExtensionValidator])

    class Meta:
        model = Campaign
        fields = ['title', 'description', 'image']


class CampaignDetailSerializer(CampaignListSerializer):

    class Meta(CampaignListSerializer.Meta):
        fields = ['id', 'scenarios'] + CampaignListSerializer.Meta.fields
