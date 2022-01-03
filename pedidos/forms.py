from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import EmailField

from django.forms import ModelForm
from .models import *

class UserRegisterForm(UserCreationForm):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=200,help_text='Calle,Numero,Colonia,Referencias')
    username=forms.CharField(error_messages={'subject':'usuario ya existente'})
    telefono=forms.CharField( max_length=10,help_text='Es necesario ingresar lada (686)')
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput,help_text='Minimo 8 caracteres',error_messages={'required':'usuario ya existente'})
    password2=forms.CharField(label='Confirma contraseña',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password1','password2','direccion','nombre','telefono']
        help_texts = {
            
            'username': 'Un usuario con el cual iniciara secion',
            

        }


class agregarform(ModelForm):
    class Meta:
        model=servicio
        exclude = ['tlim1','tlim2','tlim3','tlim4','precio','created','updated','calif']


        

        

#{{ form.as_p }}