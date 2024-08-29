from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com este username')
        else:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()    
            return HttpResponse('Usuário Cadastrado com sucesso.')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 

    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        
        if user:

            login_django(request, user)
            return render(request, 'alerta-autenticado.html')
            
        else:
            return render(request, 'alerta-usuario-nao-encontrado.html')

def logout_view(request):
    logout(request)  # Encerra a sessão do usuário
    # return redirect('logout')
    return render(request, 'logout.html')