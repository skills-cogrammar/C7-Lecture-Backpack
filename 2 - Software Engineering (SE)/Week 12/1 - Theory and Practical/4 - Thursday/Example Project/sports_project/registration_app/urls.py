from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (register_user, logout_user,
                    sport_registration, registrants, delete_registration)

urlpatterns = [
    path('', registrants, name='registrants'),
    path('register/', register_user, name='register_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', sport_registration, name='sport_registration'),
    path('registrants/delete/<int:id>', delete_registration, name='delete_registrant'),
]