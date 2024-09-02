from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Equipamentos, Inimigos
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import InimigosForms

def home(request):
    return render(request, 'gerenciador_industriawayne/home.html')

@login_required(login_url='/login/login')
def cadastrar_equipamento(request):
    return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html')

@login_required(login_url='/login/login')
def cadastrar_inimigos(request):
    form = InimigosForms(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return render(request, 'gerenciador_industriawayne/cadastrar_inimigos.html', {'form': form})

@login_required(login_url='/login/login')
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

    return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html', {'mensagem':'Equipamento salvo com sucesso.'})
    success_url = reverse_lazy('cadastrar_equipamentos')

@login_required(login_url='/login/login')
def listar_equipamentos(request):
    equipamentos = Equipamentos.objects.all()  # Recupera todos os equipamentos do banco de dados
    return render(request, 'gerenciador_industriawayne/listar_equipamentos.html', {'equipamentos': equipamentos})

class editar_equipamento(UpdateView):
    model = Equipamentos
    fields = ['nome', 'descricao', 'data', 'usuario_atual','status', 'localizacao']
    template_name = 'gerenciador_industriawayne/editar_equipamento.html'
    success_url = reverse_lazy('listar_equipamentos')  # Redireciona para a lista após edição

    def form_valid(self, form):
        # messages.success(self.request, 'Equipamento atualizado com sucesso!')
        return super().form_valid(form)

@login_required(login_url='/login/login')
def remover_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
    
    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_equipamentos')  # Redireciona para a lista de equipamentos após exclusão
    
    return render(request, 'gerenciador_industriawayne/remover_equipamento.html', {'equipamento': equipamento})


@login_required(login_url='/login/login')

def listar_inimigos(request):
    inimigos = Inimigos.objects.all()  # Recupera todos os equipamentos do banco de dados
    return render(request, 'gerenciador_industriawayne/listar_inimigos.html', {'inimigos': inimigos})

class editar_inimigo(UpdateView):
    model = Inimigos
    fields = ['nome_inimigo', 'sexo', 'super_poder', 'armas', 'grau_de_perigo', 'descricao', 'capturado','data_captura','localizacao']
    template_name = 'gerenciador_industriawayne/editar_inimigo.html'
    success_url = reverse_lazy('listar_inimigos')  # Redireciona para a lista após edição

    def form_valid(self, form):
        # messages.success(self.request, 'Inimigo atualizado com sucesso!')
        return super().form_valid(form)

@login_required(login_url='/login/login')
def remover_inimigo(request, inimigo_id):
    inimigo = get_object_or_404(Inimigos, id=inimigo_id)
    
    if request.method == 'POST':
        inimigo.delete()
        return redirect('listar_inimigos')  # Redireciona para a lista de inimigos após exclusão
    
    return render(request, 'gerenciador_industriawayne/remover_inimigo.html', {'inimigo': inimigo})