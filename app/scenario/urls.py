"""
Url mappings for scenarios.
"""
from django.urls import path
from scenario.views import ScenarioViewSet

app_name = 'scenario'

urlpatterns = [
    # scenario routing
    path(
            'campaign/<int:campaign_id>/scenario/',
            ScenarioViewSet.as_view(
                {
                    'post': 'create',
                }
            ),
            name='scenario-create'
        ),
    path(
        'campaign/<int:campaign_id>/scenario/<int:id>/',
        ScenarioViewSet.as_view(
            {
                'patch': 'partial_update',
                'delete': 'destroy'
            }
        ),
        name='scenario-update'
    )
]
