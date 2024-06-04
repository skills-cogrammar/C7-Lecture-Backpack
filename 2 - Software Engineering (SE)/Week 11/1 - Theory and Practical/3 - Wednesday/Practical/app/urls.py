from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.user_list, name = "home"),
    path("hello/", views.hello, name = "hello"),
    path('add/', views.add_user, name = "add"),
    path('edit/<id>', views.edit_user, name = "edit"),
    path('delete/<eid>', views.delete_user, name = "delete"),
    path('view/<eid>', views.view_user, name = "view"),
]