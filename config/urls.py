from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('api/tasks/', include('tasks.urls')),
    path('api/dashboard/', include('dashboard.urls')),
]
