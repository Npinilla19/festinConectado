from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cuenta creada exitosamente para {form.cleaned_data["username"]}!')
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})