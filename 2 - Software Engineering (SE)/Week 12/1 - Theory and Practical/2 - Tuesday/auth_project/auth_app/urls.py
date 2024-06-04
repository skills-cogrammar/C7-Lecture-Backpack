# auth_app/urls.py

from django.urls import path
from auth_app import views as auth_views
# from .views import register, login_view, logout_view, protected_view
# from . import views

urlpatterns = [
    path('', auth_views.index, name='index'),
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('protected/', auth_views.protected_view, name='protected'),
]
