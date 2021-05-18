from .models import Food, Vote
from django import forms

class addFood(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodImage', 
                    'foodName', 
                    'foodManufactureDate',
                    'foodExpirationDate',
                    'foodPrice']
