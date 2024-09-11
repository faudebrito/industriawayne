from django.db import models
import datetime

class Equipamentos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField(default=datetime.datetime.now)
    usuario_atual=models.CharField(max_length=100)
    choices_status = (('Em uso', 'Em uso'), 
                      ('Manutenção', 'Manutenção'),)
    status = models.CharField(max_length=12, choices=choices_status)

    choices_localizacao = (('Garagem Batcaverna', 'Garagem Batcaverna'), 
                           ('Armário 01', 'Armário 01'),
                           ('Armário 02', 'Armário 02'),
                           ('Oficina', 'Oficina'),
                           ('Emprestado Polícia', 'Emprestado Polícia'),
                           ('Com o usuário', 'Com o usuário'),)
    localizacao = models.CharField(max_length=25, choices=choices_localizacao)
    imagem = models.ImageField(upload_to= "images/", null = True, blank=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

class Inimigos(models.Model):
    id = models.AutoField(primary_key=True)
    nome_inimigo = models.CharField(max_length=100, default=None)
    choices_sexo = (('Masculino', 'Masculino'), 
                    ('Feminino', 'Feminino'),
                    ('Misógeno', 'Misógeno'),
                    ('Extraterrestre', 'Extraterrestre',) )
    sexo = models.CharField(max_length=15, choices=choices_sexo)
    super_poder = models.CharField(max_length=100, default=None)
    armas = models.CharField(max_length=50, default=None)
    choices_perigo = (('Baixa Periculosidade', 'Baixa Periculosidade'), 
                      ('Média Periculosidade', 'Média Periculosidade'), 
                      ('Alta Periculosidade', 'Alta Periculosidade',))
    grau_de_perigo = models.CharField(max_length=22, choices=choices_perigo)
    descricao = models.CharField(max_length=500, default=None)
    capturado = models.BooleanField(default=False)
    data_captura = models.DateField(default=datetime.datetime.now)
    choices_localizacao_inimigo = (('Foragido', 'Foragido'), 
                           ('Prisão Gothan City', 'Prisão Gothan City'),
                           ('Prisão Federal', 'Prisão Federal'),)
    localizacao = models.CharField(max_length=25, choices=choices_localizacao_inimigo)
    imagem = models.ImageField(upload_to= "images/", null = True, blank=True)

    class Meta:
        verbose_name = 'Inimigo'
        verbose_name_plural = 'Inimigos'


class Metas(models.Model):
    id = models.AutoField(primary_key=True)
    nome_meta = models.CharField(max_length=100, default=None)
    responsavel = models.CharField(max_length=100, default=None)
    descricao = models.CharField(max_length=500, default=None)
    data_prazo = models.DateField(default=datetime.datetime.now)
    choices_status_metas = (('Aguardando data/prazo', 'Aguardando data/prazo'), 
                            ('Concluída', 'Concluída'),)
    status = models.CharField(max_length=25, choices=choices_status_metas)

    class Meta:
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'