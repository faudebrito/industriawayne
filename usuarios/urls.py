from django.urls import path
from . import views

urlpatterns= [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar_grupos/', views.listar_grupos, name='listar_grupos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
]