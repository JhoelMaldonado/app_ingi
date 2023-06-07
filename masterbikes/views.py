from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def mostrar_inicio(request):
    return render(request, 'inicio.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
                #login(request, user)
            return redirect('/')
    return render(request, 'registro.html',data)