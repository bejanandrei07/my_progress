from django import forms
from .models import Measurements

class MeasurementsForms(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = [
            'weight', 'height', 'age', 'biceps', 'triceps',
            'shoulders', 'chest', 'waist', 'hips', 'thigs', 'calves'
        ]

        labels = {
            'weight': 'Weight (kg)',
            'height': 'Height (cm)',
            'age': 'Age',
            'biceps': 'Biceps (cm)',
            'triceps': 'Triceps (cm)',
            'shoulders': 'Shoulders (cm)',
            'chest': 'Chest (cm)',
            'waist': 'Waist (cm)',
            'hips': 'Hips (cm)',
            'thigs': 'Thighs (cm)',
            'calves': 'Calves (cm)',
        }