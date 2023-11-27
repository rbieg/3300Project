from django.forms import ModelForm
from .models import Appliance, Ingredient, LoggedUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class ApplianceForm(ModelForm):
    class Meta:
        model = Appliance
        fields = ('name', 'description', 'heat_setting')

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'cooking_method')

class CreateUserForm(UserCreationForm):
    class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

class LoggedUserForm(ModelForm):
     class Meta:
          model = LoggedUser
          fields = '__all__'
          exclude = ['user']

class RememberMeAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )