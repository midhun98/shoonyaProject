from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('retreats', views.RetreatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
