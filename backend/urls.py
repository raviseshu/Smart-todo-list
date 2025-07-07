from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Smart Todo List!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('context/', include('apps.context.urls')),
    path('categories/', include('apps.categories.urls')),
    path('ai/', include('apps.ai.urls')),
    path('', home, name='home'),  # This line adds a root URL
]
