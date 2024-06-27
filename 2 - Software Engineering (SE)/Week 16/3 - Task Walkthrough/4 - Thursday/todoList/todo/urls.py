from django.urls import path
from .views import get, get_all, create, update, delete

urlpatterns = [
    path('', get_all, name='todos'),
    path('<int:pk>', get, name='todo'),
    path('new/', create, name='create_todo'),
    path('<int:pk>/edit', update, name='update_todo'),
    path('<int:pk>/delete', delete, name='delete_todo')
]