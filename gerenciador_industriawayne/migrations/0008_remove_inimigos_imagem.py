# Generated by Django 5.0.8 on 2024-08-23 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_industriawayne', '0007_inimigos_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inimigos',
            name='imagem',
        ),
    ]
