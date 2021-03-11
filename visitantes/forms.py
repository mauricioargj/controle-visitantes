from django import forms
from django.db.models import fields
from django.db.models.base import Model
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento", "numero_casa",
            "placa_veiculo"
        ]

        error_messages = {
            "nome_completo": {
                "required": "O Nome Completo do Visitante é Obrigatório para o Registro."
            },
            "cpf": {
                "required": "O CPF do Visitante é Obrigatório para o Registro."
            },
            "data_nascimento": {
                "required": "A Data de Nascimento do Visitante é Obrigatória para o Registro.",
                "invalid": "Por Favor, Informe um Formato Válido para a Data de Nascimento. (DD/MM/AAAA)"
            },
            "numero_casa": {
                "required": "Por Favor, Informe o Número da Casa a ser Visitada."
            }
        }
