"""
Views for handling
Scenario, Npcs and Monster
APIs
"""
import sys

from rest_framework import viewsets, status
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from scenario.models import Scenario, Npc, Monster
from scenario import serializers
from campaign.models import Campaign
from django.shortcuts import get_object_or_404


class ScenarioViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    """Viewset to handle list and create actions."""
    serializer_class = serializers.ScenarioSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Scenario.objects.all()

    def get_queryset(self):
        campaign_id = self.kwargs.get('campaign_id')

        if campaign_id is None:
            return self.queryset.none()

        return self.queryset.filter(campaign__id=campaign_id).order_by('order')

    def perform_create(self, serializer):
        campaign_id = self.kwargs.get('campaign_id')

        if campaign_id is not None:
            campaign = get_object_or_404(Campaign, id=campaign_id)
            scenario = serializer.save(campaign=campaign)
            campaign.scenarios.add(scenario)
        else:
            return Response({'error': 'campaign_id is required'}, status=status.HTTP_400_BAD_REQUEST)


class ScenarioModifyViewSet(generics.RetrieveUpdateDestroyAPIView):
    """Viewset to handle retrieve, update and destroy actions."""
    serializer_class = serializers.ScenarioDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Scenario.objects.all()

    def get_queryset(self):
        campaign_id = self.kwargs.get('campaign_id')
        scenario_id = self.kwargs.get('pk')

        if not campaign_id or not scenario_id: return self.queryset.none()

        return self.queryset.filter(id=scenario_id, campaign__id=campaign_id).order_by('order')


class NpcViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NpcDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Npc.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.NpcSerializer

        return self.serializer_class

    @action(detail=True, methods=['get'], url_path='move_to_scenario/<int:scenario_id>')
    def move_npc_to_scenario(self, request, pk=None, scenario_id=None):
        """Adds an npc to a scenario"""
        scenario = get_object_or_404(Scenario, id=scenario_id)
        npc = get_object_or_404(Npc, id=pk)

        scenario.npcs.add(npc)
        return Response({'message': 'Npc moved to scenario successfully'}, status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='remove_from_scenario/<int:scenario_id>')
    def remove_npc_from_scenario(self, request,  pk=None, scenario_id=None):
        """Removes an npc from a scenario"""
        scenario = get_object_or_404(Scenario, id=scenario_id)
        npc = get_object_or_404(Npc, id=pk)

        scenario.npcs.remove(npc)
        return Response({'message': 'Npc removed from scenario successfully'}, status.HTTP_200_OK)


class MonsterViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MonsterDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Monster.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MonsterSerializer

        return self.serializer_class

    @action(detail=True, methods=['get'], url_path='move_to_scenario/<int:scenario_id>')
    def move_monster_to_scenario(self, request, pk=None, scenario_id=None):
        """Adds a monster to a scenario"""
        scenario = get_object_or_404(Scenario, id=scenario_id)
        monster = get_object_or_404(Monster, id=pk)

        scenario.monsters.add(monster)
        return Response({'message': 'Monsters moved to scenario successfully.'}, status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='remove_from_scenario/<int:scenario_id>')
    def remove_monster_from_scenario(self, request, pk=None, scenario_id=None):
        """Remove a monster from a scenario"""
        scenario = get_object_or_404(Scenario, id=scenario_id)
        monster = get_object_or_404(Monster, id=pk)

        scenario.monsters.remove(monster)
        return Response({'message': 'Monster removed from scenario successfully.'}, status.HTTP_200_OK)
