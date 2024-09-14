
from django.contrib import admin
from django.urls import path, include
from gerenciador_industriawayne import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('login/', include('usuarios.urls')),

    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('cadastrar_inimigos/', views.cadastrar_inimigos, name='cadastrar_inimigos'),
    path('cadastrar_metas/', views.cadastrar_meta, name='cadastrar_metas'),
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
    path('equipamentos/remover/<int:equipamento_id>/', views.remover_equipamento, name='remover_equipamento'),
    path('equipamentos/editar/<int:pk>/', views.editar_equipamento.as_view(), name='editar_equipamento'),
    path('inimigos/', views.listar_inimigos, name='listar_inimigos'),
    path('inimigos/remover/<int:inimigo_id>/', views.remover_inimigo, name='remover_inimigo'),
    path('inimigos/editar/<int:pk>/', views.editar_inimigo.as_view(), name='editar_inimigo'),
    path('metas/', views.listar_metas, name='listar_metas'),
    path('metas/remover/<int:meta_id>/', views.remover_meta, name='remover_meta'),
    path('metas/editar/<int:pk>/', views.editar_meta.as_view(), name='editar_meta'),
    
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)