"""
Views for handling
Scenario, Npcs and Monster
APIs
"""
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from campaign.models import Campaign
from scenario.models import Scenario
from scenario.serializers import ScenarioCreateUpdateSerializer


class ScenarioViewSet(mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    Webservice for scenario objects.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ScenarioCreateUpdateSerializer
    queryset = Scenario.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        campaign_id = self.kwargs.get('campaign_id', None)

        if campaign_id:
            campaign = get_object_or_404(Campaign, id=campaign_id, user=self.request.user)
            serializer.save(campaign=campaign)

    def perform_update(self, serializer):
        campaign_id = self.kwargs.get('campaign_id', None)

        if campaign_id:
            campaign = get_object_or_404(Campaign, id=campaign_id, user=self.request.user)
            serializer.save(campaign=campaign)

