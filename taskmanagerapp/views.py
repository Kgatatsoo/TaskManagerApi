from rest_framework import viewsets, permissions
from .models import taskmanagerapp
from .serializers import taskmanagerappserializer

class taskmanagerappViewset(viewsets.ModelViewSet):
 serializer_class = taskmanagerappserializer
 permission_classes = [permissions.IsAuthenticated]

 def get_queryset(self):
    return taskmanagerapp.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


