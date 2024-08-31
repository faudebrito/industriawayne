from django.db import models
import datetime
# from backend.core.models import TimeStampedModel

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
    nome_inimigo = models.CharField(max_length=100, default=None)
    sexo = models.CharField(max_length=50, default=None)
    super_poder = models.CharField(max_length=100, default=None)
    armas = models.CharField(max_length=50, default=None)
    grau_de_perigo = models.CharField(max_length=50, default=None)
    descricao = models.CharField(max_length=500, default=None)
    capturado = models.BooleanField(default=False)
    data_captura = models.DateField(default=datetime.datetime.now)
    localizacao = models.CharField(max_length=50, default=None)
    imagem = models.ImageField(upload_to="static/gerenciador_industriawayne/css/images", null = True, blank=True)

# class Expense(TimeStampedModel):
#     photo = models.ImageField(upload_to="", null = True, blank=True)

