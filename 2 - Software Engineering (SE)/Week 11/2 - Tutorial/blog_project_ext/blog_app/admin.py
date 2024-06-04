# blog_app/admin.py

from django.contrib import admin
from .models import BlogPost

# Register your models here.
admin.site.register(BlogPost)
