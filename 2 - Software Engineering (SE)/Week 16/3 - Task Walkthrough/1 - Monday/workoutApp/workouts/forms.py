from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = ['name','sets','description','creator']