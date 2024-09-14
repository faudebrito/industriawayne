from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Equipamentos, Inimigos, Metas
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import InimigosForms
from .forms import EquipamentosForms
from .forms import MetasForms
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    return render(request, 'gerenciador_industriawayne/home.html')
@login_required(login_url='/login/login')
def cadastrar_equipamento(request):

    if not request.user.has_perm('gerenciador_industriawayne.add_equipamentos'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        form = EquipamentosForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento Cadastrado com sucesso!')
        return render(request, 'gerenciador_industriawayne/cadastrar_equipamento.html', {'form': form})

@login_required(login_url='/login/login')
def listar_equipamentos(request):
    if not request.user.has_perm('gerenciador_industriawayne.view_equipamentos'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    
    else:
        equipamentos = Equipamentos.objects.all()  # Recupera todos os equipamentos do banco de dados
        paginator = Paginator(equipamentos, 6)
        page_number = request.GET.get('page')  # Captura o número da página na URL
        page_obj = paginator.get_page(page_number)		
        # Recupera todos os equipamentos do banco de dados
        return render(request, 'gerenciador_industriawayne/listar_equipamentos.html', {'equipamentos': equipamentos, 'page_obj': page_obj})

class editar_equipamento(UpdateView):
    model = Equipamentos
    fields = ['nome', 'descricao', 'data', 'usuario_atual','status', 'localizacao', 'imagem']
    template_name = 'gerenciador_industriawayne/editar_equipamento.html'
    success_url = reverse_lazy('listar_equipamentos')  # Redireciona para a lista após edição

    def form_valid(self, form):
        # messages.success(self.request, 'Equipamento atualizado com sucesso!')
        return super().form_valid(form)
    
@login_required(login_url='/login/login')
def remover_equipamento(request, equipamento_id):
    if not request.user.has_perm('gerenciador_industriawayne.delete_equipamentos'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
        if request.method == 'POST':
            equipamento.delete()
            return redirect('listar_equipamentos')  # Redireciona para a lista de equipamentos após exclusão
    
        return render(request, 'gerenciador_industriawayne/remover_equipamento.html', {'equipamento': equipamento})

@login_required(login_url='/login/login')
def cadastrar_inimigos(request):
    if not request.user.has_perm('gerenciador_industriawayne.add_inimigos'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        form = InimigosForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inimigo Cadastrado com sucesso!')
        return render(request, 'gerenciador_industriawayne/cadastrar_inimigos.html', {'form': form})

@login_required(login_url='/login/login')
def listar_inimigos(request):
    if not request.user.has_perm('gerenciador_industriawayne.view_inimigos'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        inimigos = Inimigos.objects.all()  # Recupera todos os inimigos do banco de dados
        paginator = Paginator(inimigos, 3)
        page_number = request.GET.get('page')  # Captura o número da página na URL
        page_obj = paginator.get_page(page_number)		
        return render(request, 'gerenciador_industriawayne/listar_inimigos.html', {'inimigos': inimigos, 'page_obj': page_obj})

class editar_inimigo(UpdateView):
    model = Inimigos
    fields = ['nome_inimigo', 'sexo', 'super_poder', 'armas', 'grau_de_perigo', 'descricao', 'capturado','data_captura','localizacao', 'imagem']
    template_name = 'gerenciador_industriawayne/editar_inimigo.html'
    success_url = reverse_lazy('listar_inimigos')  # Redireciona para a lista após edição

    def form_valid(self, form):
        # messages.success(self.request, 'Inimigo atualizado com sucesso!')
        return super().form_valid(form)

@login_required(login_url='/login/login')
def remover_inimigo(request, inimigo_id):
    if not request.user.has_perm('gerenciador_industriawayne.delete_inimigos'):
    # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        inimigo = get_object_or_404(Inimigos, id=inimigo_id)
        if request.method == 'POST':
            inimigo.delete()
            return redirect('listar_inimigos')  # Redireciona para a lista de inimigos após exclusão
        return render(request, 'gerenciador_industriawayne/remover_inimigo.html', {'inimigo': inimigo})

@login_required(login_url='/login/login')
def cadastrar_meta(request):
    if not request.user.has_perm('gerenciador_industriawayne.add_metas'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        form = MetasForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Meta Cadastrada com sucesso!')
        return render(request, 'gerenciador_industriawayne/cadastrar_metas.html', {'form': form})

@login_required(login_url='/login/login')
def listar_metas(request):
    if not request.user.has_perm('gerenciador_industriawayne.view_metas'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        metas = Metas.objects.all()  # Recupera todos os equipamentos do banco de dados
        return render(request, 'gerenciador_industriawayne/listar_metas.html', {'metas': metas})

class editar_meta(UpdateView):
    model = Metas
    fields = ['nome_meta', 'responsavel', 'descricao', 'data_prazo','status']
    template_name = 'gerenciador_industriawayne/editar_meta.html'
    success_url = reverse_lazy('listar_metas')  # Redireciona para a lista após edição

    def form_valid(self, form):
        # messages.success(self.request, 'Meta atualizada com sucesso!')
        return super().form_valid(form)

@login_required(login_url='/login/login')

def remover_meta(request, meta_id):
    if not request.user.has_perm('gerenciador_industriawayne.delete_metas'):
        # Adiciona uma mensagem de erro
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('home')
    else:
        meta = get_object_or_404(Metas, id=meta_id)
        
        if request.method == 'POST':
            meta.delete()
            return redirect('listar_metas')  # Redireciona para a lista de metas após exclusão
        
        return render(request, 'gerenciador_industriawayne/remover_meta.html', {'meta': meta})