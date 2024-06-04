from django.urls import path
from .views import view_home, welcome, sports

urlpatterns = [
    path('', view_home, name='home'),
    path('welcome/', welcome, name='welcome'),
    path('sports/', sports, name='sports'),
]