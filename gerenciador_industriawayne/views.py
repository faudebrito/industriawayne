from django.shortcuts import render
from django.http import HttpResponse


def cadastrar_equipamento(request):
    return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html')

