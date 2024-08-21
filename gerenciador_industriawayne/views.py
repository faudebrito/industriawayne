from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipamentos
from .models import Inimigos
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'gerenciador_industriawayne/base.html')

@login_required(login_url='/configuracao/login')
def cadastrar_equipamento(request):
    return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html')

@login_required(login_url='/configuracao/login')
def cadastrar_inimigos(request):
    return render(request, 'gerenciador_industriawayne/cadastrar_inimigos.html')

@login_required(login_url='/configuracao/login')
def processar_cadastro(request):
    nome=request.POST.get('nome')
    descricao=request.POST.get('descricao')
    data=request.POST.get('data')
    usuario_atual=request.POST.get('usuario_atual')
    status=request.POST.get('status')
    localizacao=request.POST.get('localizacao')

    equipamento = Equipamentos(
        nome=nome,
        descricao=descricao,
        data=data,
        usuario_atual=usuario_atual,
        status=status,
        localizacao=localizacao,
        )
    
    equipamento.save()

    return HttpResponse("Equipamento salvo com sucesso!")

@login_required(login_url='/configuracao/login')
def listar_equipamentos(request):
    equipamentos = Equipamentos.objects.all()  # Recupera todos os equipamentos do banco de dados
    return render(request, 'gerenciador_industriawayne/listar_equipamentos.html', {'equipamentos': equipamentos})

@login_required(login_url='/configuracao/login')
def processar_cadastro_inimigos(request):
    nome_inimigo=request.POST.get('nome_inimigo')
    sexo=request.POST.get('sexo')
    super_poder=request.POST.get('super_poder')
    armas=request.POST.get('armas')
    grau_de_perigo=request.POST.get('grau_de_perigo')
    descricao=request.POST.get('descricao')
    capturado=request.POST.get('capturado')
    data_captura=request.POST.get('data_captura')
    localizacao=request.POST.get('localizacao')

    inimigo = Inimigos(
        nome_inimigo=nome_inimigo,
        sexo=sexo,
        super_poder=super_poder,
        armas=armas,
        grau_de_perigo=grau_de_perigo,
        descricao=descricao,
        capturado=capturado,
        data_captura=data_captura,
        localizacao=localizacao,
        )
    
    inimigo.save()

    return HttpResponse("Inimigo salvo com sucesso!")

@login_required(login_url='/configuracao/login')
def listar_inimigos(request):
    inimigos = Inimigos.objects.all()  # Recupera todos os equipamentos do banco de dados
    return render(request, 'gerenciador_industriawayne/listar_inimigos.html', {'inimigos': inimigos})