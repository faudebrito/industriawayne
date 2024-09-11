from django.urls import path
from . import views

urlpatterns= [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar_grupo/', views.listar_grupo, name='listar_grupo'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]