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
class encuesta(ModelForm):
    class Meta:
        model=Cuentas
        exclude = ['create','entraporcen']
        fields=('ganper','conce','importa','canti')
        widgets={
            
            
            'ganper': forms.CheckboxInput(attrs={'class':"form-check-input", "id": "ganper","value":1}),
            'conce': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el concepto del gasto'}),
            'importa': forms.CheckboxInput(attrs={'class':"form-check-input", "id": "importa","value":1}),
            'canti': forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }
class deudarocio(ModelForm):
    class Meta:
        model=Gastos
        exclude = ['created','entraporcen']
        fields=('ganoper','concep','cantidad','importancia')
        widgets={
            
            
            'ganoper': forms.CheckboxInput(attrs={'class':"form-check-input", "id": "ganoper","value":1}),
            'concep': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el concepto del pago'}),
            'importancia': forms.CheckboxInput(attrs={'class':"form-check-input", "id": "importancia","value":1}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }

        

        

#{{ form.as_p }}