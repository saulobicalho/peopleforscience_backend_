from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from clients.models import Cliente
from clients.views import lista_clientes


class TestClientViews(TestCase):

    def setUp(self):
        #inicializa um usuario para satisfazer o @login_required da view de listagem de clientes
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        self.clientes_inseridos = []
        self.clientes_inseridos.append(Cliente.clientes.create(nome = "Joana", endereco = 'rua x', telefone='2222'))
        self.clientes_inseridos.append(Cliente.clientes.create(nome = "Josefina", endereco = 'rua y', telefone='3333'))

    def test_lista_clientes(self):


        #faz a requisicao
        resposta = self.client.get(reverse('client_lista_clientes'))

        #obter dados da resposta


        dados_resposta = resposta.context

        #realiza o teste
        lst_clientes_resposta = dados_resposta["clientes"]

        for cliente_resposta in lst_clientes_resposta:
            #procura clientes na lista de resposta
            encontrou = False
            for cliente_inserido in self.clientes_inseridos:
                if cliente_resposta.id == cliente_inserido.id:
                    encontrou = True
                    self.assertEqual(cliente_resposta.nome,cliente_inserido.nome,
                                     "Nome inesperado ao listar clientes")
            self.assertTrue(encontrou, f"O cliente {cliente_resposta} não foi encontrado")
        self.assertEqual(len(self.clientes_inseridos), len(lst_clientes_resposta),
                         "O numero de clientes inseridos é diferente do numero de clientes retornados")


    def test_cliente_novo(self):


        #faz a requisicao
        str_url = reverse('client_cliente_novo')
        self.client.post(str_url, {"nome": "Empresa x", "endereco": "rua x", "telefone": "1111"})

        #realiza o teste
        lstClienteX = Cliente.clientes.filter(nome="Empresa x",
                                              endereco = "rua x",
                                              telefone = "1111")
        self.assertNotEquals(0,len(lstClienteX),
                             "Nao foi possivel encontrar a instancia inserida")
        self.assertEquals(1,len(lstClienteX),
                          "A instancia foi inserida mais de uma vez")


    def test_cliente_update(self):


        #faz a requisicao
        id_atualizar = self.clientes_inseridos[0].id
        str_url = reverse('client_cliente_update', kwargs={"id":id_atualizar})
        self.client.post(str_url, {"nome": "Empresa x2", "endereco": "rua x2", "telefone": "2222"})

        #realiza o teste
        lstClienteX = Cliente.clientes.filter(id=id_atualizar,
                                              nome = "Empresa x2",
                                              endereco = "rua x2",
                                              telefone = "2222")
        self.assertEquals(1,len(lstClienteX),
                          "A instancia foi inserida mais de uma vez")


