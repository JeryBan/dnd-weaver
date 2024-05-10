"""
Views for handling campaign API.
"""
from rest_framework import viewsets, status
from rest_framework import authentication, permissions
from rest_framework.response import Response
from campaign.models import Campaign
from campaign import serializers


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CampaignSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Campaign.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return serializers.CampaignDetailSerializer

        return serializers.CampaignSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
