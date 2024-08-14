from django.db import models
import datetime

class Equipamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField(default=datetime.datetime.now)
    usuario_atual=models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50, default=None)
    # imagem = models.CharField(max_length=100)

class Inimigos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    super_poder = models.CharField(max_length=100)
    grau_de_perigo = models.CharField(max_length=50)
    capturado = models.BooleanField(default=False)
    # imagem = models.CharField(max_length=100)



