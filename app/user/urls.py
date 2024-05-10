"""
User url mappings.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

app_name = 'user'
router = DefaultRouter()

router.register('user', views.UserViewSet)
router.register('user/players', views.PlayerReadOnlyViewSet)

urlpatterns = [
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('', include(router.urls))
]
