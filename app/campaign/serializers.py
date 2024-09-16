"""
Serializers for handling campaign data.
"""
from rest_framework import serializers, validators
from campaign.models import Campaign
from core.validators import FileExtensionValidator
from scenario.serializers import ScenarioSerializer


class CampaignSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    # image = serializers.FileField(validators=[FileExtensionValidator], required=False, allow_null=True)
    image = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    scenarios = ScenarioSerializer(many=True, required=False)

    class Meta:
        model = Campaign
        fields = ['id', 'title', 'description', 'image', 'scenarios']
        read_only_fields = ['id', 'scenarios']


class CampaignCreateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Campaign
        fields = ['id', 'title', 'description', 'image']
