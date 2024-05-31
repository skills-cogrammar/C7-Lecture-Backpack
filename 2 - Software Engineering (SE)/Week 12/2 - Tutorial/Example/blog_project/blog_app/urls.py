# blog_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
]
