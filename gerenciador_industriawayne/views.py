from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Equipamentos


def cadastrar_equipamento(request):
    return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html')

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

def listar_equipamentos(request):
    equipamentos = Equipamentos.objects.all()  # Recupera todos os equipamentos do banco de dados
    return render(request, 'gerenciador_industriawayne/listar_equipamentos.html', {'equipamentos': equipamentos})

