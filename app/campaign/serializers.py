"""
Serializers for handling campaign data.
"""
from rest_framework import serializers
from campaign.models import Campaign


class CampaignListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['title', 'description', 'image']


class CampaignDetailSerializer(CampaignListSerializer):

    class Meta(CampaignListSerializer.Meta):
        fields = ['id', 'scenarios'] + CampaignListSerializer.Meta.fields
