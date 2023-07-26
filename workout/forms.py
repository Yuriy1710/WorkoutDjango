from django import forms
from .models import *


class CreateExerciseForm(forms.ModelForm):
    
    class Meta:
        model = CreateExercise
        fields = ['name']
        
        labels = {
          'name': 'Enter exercise name'
        }

