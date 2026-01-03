from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import taskmanagerappViewset

router = DefaultRouter()
router.register('taskmanagerapp', taskmanagerappViewset, basename= 'taskmanagerapp')

urlpatterns = [
    path('', include(router.urls)),
]