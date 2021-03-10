from django import forms
from django.db.models import fields
from django.db.models.base import Model
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__"
