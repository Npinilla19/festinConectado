from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


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


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, "Credenciales incorrectas")
        else:
            messages.error(request, "Formulario inválido")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})