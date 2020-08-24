from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Avaliacao
from django import forms
from django.forms import TextInput


class AvaliacaoForm(ModelForm):

    class Meta:
        model = Avaliacao
        fields = '__all__'
