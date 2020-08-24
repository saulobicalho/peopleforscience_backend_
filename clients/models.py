from django.db import models
from django.db.models import QuerySet


class ClienteQuerySet(QuerySet):
    def clientes(self):
        return self.all()

    def cliente_atual(self,client_id):
        return self.get(id=client_id)


class ClienteManager(models.Manager):
    def get_queryset(self):
        return ClienteQuerySet(self.model)

    def clientes(self):
        return self.get_queryset().clientes()

    def cliente_atual(self,client_id):
        return self.get_queryset().cliente_atual(client_id)



class Cliente(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)

    projeto_contratado = models.CharField(max_length=50, blank=True, null=True)

    clientes = ClienteManager()


    def __str__(self):
        return self.nome



'''need testing

    def n_projetos_cliente(self):
        return self.projeto_contratado.all.count

    def sem_projeto(self):
        if (self.n_projetos_cliente(self)==0):
            return True
        else:
            return False
'''
