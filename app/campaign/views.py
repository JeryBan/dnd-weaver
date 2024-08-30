"""
Views for handling campaign API.
"""
from rest_framework import authentication, permissions
from rest_framework import viewsets

from campaign.serializers import CampaignSerializer
from campaign.models import Campaign


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Campaign.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user,
                                    is_active=True
                                    ).order_by('id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
