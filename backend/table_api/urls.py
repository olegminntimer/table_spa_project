from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableDataViewSet

router = DefaultRouter()
router.register(r'items', TableDataViewSet, basename='tabledata')

urlpatterns = [
    path('', include(router.urls)),
]
