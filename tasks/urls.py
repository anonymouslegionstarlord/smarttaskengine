from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectCategoryViewSet, TaskItemViewSet

router = DefaultRouter()
router.register(r'projectcategorys', ProjectCategoryViewSet)
router.register(r'taskitems', TaskItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
