from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title',
                  'description',
                  'is_completed',
                  'created_by']
