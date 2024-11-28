from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'password', 'nombre', 'apellido', 'direccion', 'telefono', 'tipo_usuario']

    def save(self, commit=True):
        
        user = User.objects.create_user(
            username=self.cleaned_data['nombre_usuario'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['correo']
        )
        
       
        usuario = super().save(commit=False)
        usuario.user = user  
        if commit:
            usuario.save()  

        return usuario
