from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm


def inicio(request):
  return render(request, 'inicio.html', {})

def acerca(request):
  return render(request, 'acerca.html', {})

def empresas(request):
  return render(request, 'empresas.html', {})

def eventos(request):
  return render(request, 'eventos.html', {})

def login(request):
  return render(request, 'login.html', {})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada con éxito. ¡Puedes iniciar sesión!')
            return redirect('login')
    else:
        
        form = RegistroUsuarioForm()

    return render(request, 'registro.html', {'form': form})