from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Projeto
from .models import Cliente
from .forms import ClienteForm


@login_required()
def lista_clientes(request):
    clientes = Cliente.clientes.clientes()
    form = ClienteForm()
    return render(request, 'clients/lista_clientes.html', {'clientes': clientes, 'form': form})

@login_required()
def cliente_detail(request, id):
    data = {}
    cliente = Cliente.clientes.cliente_atual(id)
    data['cliente'] = cliente
    projetos_cliente = Projeto.projetos.projetos_cliente(id)
    data['projetos_cliente'] = projetos_cliente
    return render(request, 'clients/client_detail.html', data)


@login_required()
def cliente_novo(request):
    data = {}
    form = ClienteForm(request.POST or None)
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente criado com sucesso!')
            return redirect('client_lista_clientes')
        else:
            messages.error(request, f'Falha ao criar registro. Favor tentar novamente')
            return render(request, 'clients/cliente_novo.html', data)
    else:
        return render(request, 'clients/cliente_novo.html', data)


@login_required()
def cliente_update(request, id):
    data = {}
    cliente = Cliente.clientes.cliente_atual(id)
    form = ClienteForm(request.POST or None, instance=cliente)
    data['cliente'] = cliente
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('client_lista_clientes')
        else:
            return render(request, 'clients/update_cliente.html', data)
    else:
        return render(request, 'clients/update_cliente.html', data)


@login_required()
def cliente_delete(request, id):
    cliente = Cliente.clientes.cliente_atual(id)

    if request.method == 'POST':
        if cliente.delete():
            return redirect('client_lista_clientes')
    else:
        return render(request, 'clients/delete_confirm_cliente.html', {'cliente': cliente})
