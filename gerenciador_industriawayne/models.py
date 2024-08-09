from django.db import models

class Equipamentos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    imagem = models.CharField(max_length=100)

class Inimigos(models.Model):
    nome = models.CharField(max_length=100)
    super_poder = models.CharField(max_length=100)
    grau_de_perigo = models.CharField(max_length=50)
    capturado = models.BooleanField(default=False)
    imagem = models.CharField(max_length=100)



