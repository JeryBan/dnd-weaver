"""
Url mappings for scenarios.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from scenario import views

app_name = 'scenario'
npc_router = DefaultRouter()
monster_router = DefaultRouter()

npc_router.register('npc', views.NpcViewSet)
monster_router.register('monster', views.MonsterViewSet)

urlpatterns = [
    # scenario routing
    path('campaign/<int:campaign_id>/scenarios', views.ScenarioViewSet.as_view({'get': 'list'}), name='scenarios-list'),
    path('campaign/<int:campaign_id>/scenarios/', views.ScenarioViewSet.as_view({'post': 'create'}), name='scenario-create'),
    path('campaign/<int:campaign_id>/scenarios/<int:pk>', views.ScenarioModifyViewSet.as_view(), name='scenarios-retrieve'),
    path('campaign/<int:campaign_id>/scenarios/<int:pk>', views.ScenarioModifyViewSet.as_view(), name='scenario-update'),
    path('campaign/<int:campaign_id>/scenarios/<int:pk>', views.ScenarioModifyViewSet.as_view(), name='scenario-destroy'),
    # npc routing
    path('', include(npc_router.urls)),
    path('npc/<int:pk>/move_to_scenario/<int:scenario_id>/', views.NpcViewSet.as_view({'get': 'move_npc_to_scenario'}), name='npc-move-to-scenario'),
    path('npc/<int:pk>/remove_from_scenario/<int:scenario_id>/', views.NpcViewSet.as_view({'delete': 'remove_npc_from_scenario'}), name='npc-remove-from-scenario'),
    # monster routing
    path('', include(monster_router.urls)),
    path('monster/<int:pk>/move_to_scenario/<int:scenario_id>/', views.MonsterViewSet.as_view({'get': 'move_monster_to_scenario'}), name='monster-move-to-scenario'),
    path('monster/<int:pk>/remove_from_scenario/<int:scenario_id>/', views.MonsterViewSet.as_view({'delete': 'remove_monster_from_scenario'}), name='monster-remove-from-scenario')
]