from django import forms
from django.forms import TextInput

from .models import *


class NewClientRegForm(forms.ModelForm):
    class Meta:
        model = NewClientReg
        fields = ['firstname', 'lastname', 'password', 'password_confirmation', 'email', ]
        widgets = {
            'firstname': TextInput(attrs={'placeholder': 'Иван'}),
            'lastname': TextInput(attrs={'placeholder': 'Иванов'}),
            'password': TextInput(attrs={'placeholder': 'soHard_9ssw03d'}),
            'password_confirmation': TextInput(attrs={'placeholder': 'Повторите пароль'}),
            'email': TextInput(attrs={'placeholder': 'ivanov@mail.ru'}),
        }


class ExistedClientForm(forms.ModelForm):
    class Meta:
        model = NewClientReg
        fields = ['firstname', 'lastname', 'password', 'email', ]
        widgets = {
            'firstname': TextInput(attrs={'placeholder': 'Иван'}),
            'lastname': TextInput(attrs={'placeholder': 'Иванов'}),
            'password': TextInput(attrs={'placeholder': 'soHard_9ssw03d'}),
            'email': TextInput(attrs={'placeholder': 'ivanov@mail.ru'}),
        }


class FoodAmount(forms.Form):
    food_order_amount = forms.CharField()
