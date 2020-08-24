from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from .views import (
    lista_clientes,
    cliente_novo,
    cliente_update,
    cliente_delete,
    cliente_detail,
)

urlpatterns = [
    path('', lista_clientes, name="client_lista_clientes"),
    path('cliente-novo/', cliente_novo, name="client_cliente_novo"),
    path('cliente-update/<int:id>', cliente_update, name="client_cliente_update"),
    path('cliente-delete/<int:id>', cliente_delete, name="client_cliente_delete"),
    path('cliente-detail/<int:id>', cliente_detail, name="client_cliente_detail"),
]
