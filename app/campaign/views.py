"""
Views for handling campaign API.
"""
from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions, status
from rest_framework import viewsets
from rest_framework.response import Response

from campaign.serializers import CampaignSerializer, CampaignRetrieveSerializer
from campaign.models import Campaign
from scenario.models import Scenario, Monster, Npc


class CampaignViewSet(viewsets.ModelViewSet):
    """
    Webservice for campaign objects.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        q = Q(user=self.request.user, is_active=True)

        if self.action == 'retrieve':
            return Campaign.objects.prefetch_related(
                Prefetch(
                    'scenarios',
                    queryset=Scenario.objects.prefetch_related(
                        Prefetch(
                            'monsters',
                            queryset=Monster.objects.all()
                        ),
                        Prefetch(
                            'npcs',
                            queryset=Npc.objects.all()
                        )
                    )
                )
            ).filter(q).first()

        return Campaign.objects.filter(q).order_by('id')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CampaignRetrieveSerializer

        return CampaignSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        id = self.kwargs.get(self.lookup_field)
        campaign = get_object_or_404(Campaign, id=id)
        serializer = self.get_serializer(campaign)
        return Response(serializer.data, status=status.HTTP_200_OK)


