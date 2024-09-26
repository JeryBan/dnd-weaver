"""
Url mappings for campaign.
"""
from django.urls import path
from campaign.views import CampaignViewSet

app_name = 'campaign'

urlpatterns = [
    path(
        'campaign/overview/',
        CampaignViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='campaign'),

    path(
        'campaign/<int:id>/', CampaignViewSet.as_view(
            {
                'get': 'retrieve',
                'patch': 'partial_update',
                'delete': 'destroy'
            }
        )
    )
]
