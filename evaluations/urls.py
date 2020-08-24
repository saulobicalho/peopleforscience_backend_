from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from users import views as user_views
from .views import (
    lista_avaliacoes_consultor,
    avaliacao_novo,
    avaliacao_update,
    avaliacao_delete,
    avaliacao_detail,
)

urlpatterns = [
    path('avaliacoes_consultor/', lista_avaliacoes_consultor, name="evaluations_lista_avaliacoes_consultor"),
    path('avaliacao-novo/', avaliacao_novo, name="evaluations_avaliacao_novo"),
    path('avaliacao-detail/<int:id>', avaliacao_detail, name="evaluations_avaliacao_detail"),
    path('avaliacao-update/<int:id>', avaliacao_update, name="evaluations_avaliacao_update"),
    path('avaliacao-delete/<int:id>', avaliacao_delete, name="evaluations_avaliacao_delete"),

]
