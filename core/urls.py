from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from users import views as user_views
from .views import (
    home,
    lista_projetos_consultor,
    projeto_novo,
    projeto_update,
    projeto_delete,
    projeto_detail,
)

urlpatterns = [
    path('', home, name="core_home"),
    path('clients/', include('clients.urls')),
    path('evaluations/', include('evaluations.urls')),
    path('profile/', user_views.profile, name='profile'),
    path('projetos_consultor/', lista_projetos_consultor, name="core_lista_projetos_consultor"),
    path('projeto-novo/', projeto_novo, name="core_projeto_novo"),
    path('projeto-update/<int:id>', projeto_update, name="core_projeto_update"),
    path('projeto-delete/<int:id>', projeto_delete, name="core_projeto_delete"),
    path('projeto-detail/<int:id>', projeto_detail, name="core_projeto_detail"),
    
    
]
