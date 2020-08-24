from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet

from core.models import Projeto

class AvaliacaoQuerySet(QuerySet):
    def avaliacoes_projeto(self,projeto_id):
        return self.filter(projeto = projeto_id)

    def avaliacao_atual(self,avaliacao_id):
        return self.get(id=avaliacao_id)

    def avaliacoes_usuario(self,usuario):
        return self.filter(avaliador = usuario)


class AvaliacaoManager(models.Manager):
    def get_queryset(self):
        return AvaliacaoQuerySet(self.model)

    def avaliacoes_projeto(self,projeto_id):
        return self.get_queryset().avaliacoes_projeto(projeto_id)

    def avaliacao_atual(self,avaliacao_id):
        return self.get_queryset().avaliacao_atual(avaliacao_id)

    def avaliacoes_usuario(self,usuario):
        return self.get_queryset().avaliacoes_usuario(usuario)


class Avaliacao(models.Model):
    STATUS = (
        ('A iniciar', 'A iniciar',),
        ('Em andamento', 'Em andamento',),
        ('Finalizada', 'Finalizada',)
    )
    projeto = models.ForeignKey(Projeto, db_column="projeto", on_delete=models.DO_NOTHING)
    avaliador = models.ForeignKey(User, db_column="user", on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, choices=STATUS)

    avaliacoes = AvaliacaoManager()

    class Meta:
        verbose_name_plural= 'Avaliacoes'





