from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):

    user = models.CharField(max_length=30, unique=True)
    sport = models.CharField(max_length=25)
    team_name = models.CharField(max_length=30, unique=True)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ('ultra_register', 'User gets ultra registration')
        ]