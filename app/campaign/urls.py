"""
Url mappings for campaign.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campaign import views

app_name = 'campaign'
router = DefaultRouter()

router.register('campaign', views.CampaignViewSet)

urlpatterns = [
    path('', include(router.urls))
]