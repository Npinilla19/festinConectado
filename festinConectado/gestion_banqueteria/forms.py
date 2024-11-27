from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
   
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=250)
    telefono = forms.CharField(max_length=20)
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO)
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Confirmar Contraseña')
    username = forms.CharField(label='Nombre Usuario', )
    email = forms.EmailField(label='Correo')

    class Meta:
        model = User  
        fields = ['username', 'email', 'password1', 'password2']
              
    def save(self, commit=True):
        
        
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password1'])  
            user.save()

        
        perfil = Usuario(user=user)  
        perfil.nombre = self.cleaned_data['nombre']
        perfil.apellido = self.cleaned_data['apellido']
        perfil.direccion = self.cleaned_data['direccion']
        perfil.telefono = self.cleaned_data['telefono']
        perfil.correo = self.cleaned_data['correo']
        perfil.tipo_usuario = self.cleaned_data['tipo_usuario']
        perfil.save()  

        return user 
