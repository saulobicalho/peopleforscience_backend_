from django.contrib.auth.models import User
from django.db import models
from django.db.models import QuerySet

from clients.models import Cliente


class ProjetoQuerySet(QuerySet):
    def projetos_cliente(self,client_id):
        return self.filter(cliente = client_id)

    def projeto_atual(self,projeto_id):
        return self.get(id=projeto_id)

    def projetos_usuario(self,usuario):
        return self.filter(consultor = usuario)



class ProjetoManager(models.Manager):
    def get_queryset(self):
        return ProjetoQuerySet(self.model)

    def projetos_cliente(self,client_id):
        return self.get_queryset().projetos_cliente(client_id)

    def projeto_atual(self,projeto_id):
        return self.get_queryset().projeto_atual(projeto_id)

    def projetos_usuario(self,usuario):
        return self.get_queryset().projetos_usuario(usuario)


class Projeto(models.Model):
    STATUS = (
        ('A iniciar', 'A iniciar',),
        ('Em andamento', 'Em andamento',),
        ('Finalizado', 'Finalizado',)
    )
    nome = models.CharField(max_length=50, unique=True)
    cliente = models.ForeignKey(Cliente, db_column="cliente", on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, choices=STATUS)
    consultor = models.ManyToManyField(User)

    projetos = ProjetoManager()

    def __str__(self):
        return self.nome

    def n_consultores_projeto(self):
        return self.consultor.all.count


'''1st attempt to update a field on client, string w projectname, but not resolved how
to keep it consistent over all changes may happen on data along db operations
    def save(self, *args, **kwargs):
        if not self.pk:
            if self.cliente.sem_projeto:
                Cliente.clientes.select_for_update().filter(id = self.cliente.id)\
                    .update(projeto_contratado=self.nome)
            else:
                return
        super().save(*args, **kwargs)

'''

