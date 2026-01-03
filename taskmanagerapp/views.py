from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Automatically set the user when creating a task
        serializer.save(user=self.request.user)

# Optional home view for testing
def home(request):
    return HttpResponse("Welcome to Task Manager API")
