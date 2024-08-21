"""
URL configuration for industriawayne project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gerenciador_industriawayne import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),
    path('configuracao/', include('usuarios.urls')),
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('cadastrar_inimigos/', views.cadastrar_inimigos, name='cadastrar_inimigos'),
    path('processar_cadastro/', views.processar_cadastro, name='processar_cadastro'),
    path('equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
    path('processar_cadastro_inimigos/', views.processar_cadastro_inimigos, name='processar_cadastro_inimigos'),
    path('inimigos/', views.listar_inimigos, name='listar_inimigos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

