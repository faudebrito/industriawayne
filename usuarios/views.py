from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User as User_contrib_auth
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator

@login_required(login_url="login")
def cadastro(request):
    if not request.user.has_perm('usuarios.add_user'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        if request.method == 'GET':
            grupos = Group.objects.all()
            return render(request, 'cadastro.html', {'grupos': grupos})
        else:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            grupo = request.POST.get('grupo')
            
            user = User_contrib_auth.objects.filter(username=username).first()
            if user:
                messages.error(request, 'Já existe um usuário com este username')
                return render(request, 'alerta-usuario-erro.html')
            
            else:
                user = User_contrib_auth.objects.create_user(username=username, email=email, password=senha, first_name=first_name, last_name=last_name)
                user.save()    
                grupo_do_usuario =  Group.objects.get(name=grupo) 
                grupo_do_usuario.user_set.add(user)
                messages.success(request, 'Usuário Cadastrado com sucesso!')
                return render(request, 'alerta-usuario.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 

    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        grupo = request.POST.get('grupo')

        user = authenticate(username=username, password=senha, group=grupo)
        
        if user:

            login_django(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return render(request, 'alerta-usuario.html')
            
        else:
            messages.error(request, 'Usuário ou senha inválido ! Tente novamente')
            return render(request, 'alerta-usuario-erro.html')

def logout_view(request):
    logout(request)  # Encerra a sessão do usuário
    # return redirect('logout')
    messages.success(request, 'Logout realizado com sucesso!')
    return render(request, 'alerta-usuario.html')

@login_required(login_url='/login/login')
def listar_grupos(request):
    if not request.user.has_perm('gerenciador_industriawayne.view_group'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        grupos = Group.objects.all()  # Busca todos os grupos
        return render(request, 'cadastro.html', {'grupos': grupos})

@login_required(login_url='/login/login')
def listar_usuarios(request):
    if not request.user.has_perm('gerenciador_industriawayne.view_user'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        usuarios = User_contrib_auth.objects.all()  # Recupera todos os equipamentos do banco de dados
        paginator = Paginator(usuarios, 6)
        page_number = request.GET.get('page')  # Captura o número da página na URL
        page_obj = paginator.get_page(page_number)	
        return render(request, 'listar_usuarios.html', {'usuarios': usuarios, 'page_obj': page_obj})
