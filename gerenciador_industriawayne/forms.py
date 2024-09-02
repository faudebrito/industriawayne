from django import forms
from .models import Inimigos 

class InimigosForms(forms.ModelForm):
    class Meta:
        model=Inimigos
        fields=(
            "nome_inimigo",
            "sexo",
            "super_poder",
            "armas",
            "grau_de_perigo",
            "descricao",
            "capturado",
            "data_captura",
            "localizacao",
            "imagem",
        )
        labels = {
            "nome_inimigo": "Nome do inimigo ",
            "sexo": "sexo: ",
            "super_poder": "Super_poder: ",
            "armas": "Armas: ",
            "grau_de_perigo": "Grau de perigo: ",
            "descricao": "Descricao: ",
            "capturado": "Capturado: ",            
            "data_captura": "Data Captura: ",
            "localizacao": "Localizacao: ",
            "imagem": "Imagem: "
        }