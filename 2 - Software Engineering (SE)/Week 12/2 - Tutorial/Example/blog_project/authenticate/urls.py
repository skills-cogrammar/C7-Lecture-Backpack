from django.urls import path
from django.contrib.auth.views import LoginView
from .views import register_user, logout_user


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]