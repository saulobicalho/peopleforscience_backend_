from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    readonly_fields = [
        'projeto',
        'avaliador',
        'status',
    ]
