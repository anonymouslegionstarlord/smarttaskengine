from django.contrib import admin
from .models import ProjectCategory, TaskItem

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']

@admin.register(TaskItem)
class TaskItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'assigned_to']
    search_fields = ['title', 'status', 'priority']

