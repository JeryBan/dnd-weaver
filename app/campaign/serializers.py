"""
Serializers for handling campaign data.
"""
from rest_framework import serializers
from campaign.models import Campaign


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['title', 'description', 'image']


class CampaignDetailSerializer(CampaignSerializer):

    class Meta(CampaignSerializer.Meta):
        fields = ['id', 'scenarios'] + CampaignSerializer.Meta.fields
