from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import FoodItem, AddDate, AddDetail
from datetime import date
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}


class Additemform(forms.ModelForm):
 class Meta:
  model = FoodItem
  fields = ['Fooditem', 'Protein', 'Carbohydrates','Fat','Calories']
  widgets = {
   'Fooditem': forms.TextInput(attrs={'class':'form-control'}),
   'Protein': forms.NumberInput(attrs={'class':'form-control'}),
   'Carbohydrates': forms.NumberInput(attrs={'class':'form-control'}),
   'Fat': forms.NumberInput(attrs={'class': 'form-control'}),
   'Calories': forms.NumberInput(attrs={'class': 'form-control'}),
  }


# class AddDateForm(forms.ModelForm):
#     date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
#     class Meta:
#      model = AddDate
#      fields = '__all__'


# forms.py
from django import forms
from .models import AddDate

class AddDateForm(forms.ModelForm):
    class Meta:
        model = AddDate
        fields = ['date']
        widgets = {
            'user': forms.HiddenInput(),  # Hide the 'user' field
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)
        instance.user = user  # Set the 'user' field to the provided user
        if commit:
            instance.save()
        return instance


class AddDetailForm(forms.ModelForm):
 class Meta:
  model = AddDetail
  fields = '__all__'