from django import forms
from .models import Inimigos
from .models import Equipamentos
from .models import Metas

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
            "sexo": "Sexo ",
            "super_poder": "Super poder ",
            "armas": "Armas ",
            "grau_de_perigo": "Grau de perigo ",
            "descricao": "Descricao ",
            "capturado": "Capturado ",            
            "data_captura": "Data Captura ",
            "localizacao": "Localização ",
            "imagem": "Imagem ",
        }

class EquipamentosForms(forms.ModelForm):
    class Meta:
        model=Equipamentos
        fields=(
            "nome",
            "descricao",
            "data",
            "usuario_atual",
            "status",
            "localizacao",
            "imagem",
        )

        labels = {
            "nome": "Nome do equipamento ",
            "descricao": "Descrição ",
            "data": "Data de fabricação ",
            "usuario_atual": "Usuário atual ",
            "status": "Status ",
            "localizacao": "Localização ",
            "imagem": "Imagem "
        }

class MetasForms(forms.ModelForm):
    class Meta:
        model=Metas
        fields=(
            "nome_meta",
            "responsavel",
         )

        labels = {
            "nome_meta": "Meta ",
            "responsavel": "Responsavel ",
        }
