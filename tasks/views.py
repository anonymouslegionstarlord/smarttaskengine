from rest_framework import viewsets, permissions
from .models import ProjectCategory, TaskItem
from .serializers import ProjectCategorySerializer, TaskItemSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProjectCategory.objects.all()
    serializer_class = ProjectCategorySerializer
    permission_classes = [permissions.AllowAny]

class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer
    permission_classes = [permissions.AllowAny]

