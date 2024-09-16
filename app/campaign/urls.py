"""
Url mappings for campaign.
"""
from django.urls import path
from campaign.views import CampaignViewSet

app_name = 'campaign'

urlpatterns = [
    path('campaigns/', CampaignViewSet.as_view({'get': 'list'}), name='campaigns'),
    path('campaign/', CampaignViewSet.as_view({'post': 'create'}), name='campaign'),
    path('campaign/<int:id>', CampaignViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'}
    ), name='campaign-mod'),
]
