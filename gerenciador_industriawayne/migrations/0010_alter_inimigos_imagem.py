# Generated by Django 5.0.8 on 2024-08-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador_industriawayne', '0009_inimigos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inimigos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
