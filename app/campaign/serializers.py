"""
Serializers for handling campaign data.
"""
from rest_framework import serializers, validators
from campaign.models import Campaign
from core.validators import FileExtensionValidator
from scenario.serializers import ScenarioRetrieveSerializer


class CampaignSerializer(serializers.ModelSerializer):
    """
    Campaign Serializer for List and Update actions
    """
    title = serializers.CharField(
        required=False,
        help_text='Title'
    )
    description = serializers.CharField(
        required=False,
        help_text='Description'
    )
    image = serializers.CharField(
        required=False,
        help_text='Image Path'
    )

    class Meta:
        model = Campaign
        fields = ('id', 'title', 'description', 'image')
        read_only_fields = ['id']


class CampaignRetrieveSerializer(serializers.ModelSerializer):
    """
    Campaign Serializer for Retrieve action
    """
    title = serializers.CharField(
        required=False,
        help_text='Title'
    )
    scenarios = ScenarioRetrieveSerializer(
        many=True,
        allow_null=True,
        required=False
    )

    class Meta:
        model = Campaign
        fields = ('id', 'title', 'scenarios')
        read_only_fields = fields

