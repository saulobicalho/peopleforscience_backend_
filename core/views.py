from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ProjetoForm


@login_required()
def home(request):
    context = {'mensagem': "Bem-vindo!"}
    return render(request, 'core/index.html', context)


'''inicio views do projeto'''



@login_required()
def lista_projetos_consultor(request):
    projetos = Projeto.projetos.projetos_usuario(request.user)
    return render(request, 'core/lista_projetos_consultor.html', {'projetos': projetos})


@login_required()
def projeto_detail(request, id):
    data = {}
    projeto = Projeto.projetos.projeto_atual(id)
    return render(request, 'core/projeto_detail.html', {'projeto': projeto})


@login_required()
def projeto_novo(request):
    data = {}
    form = ProjetoForm(request.POST or None, initial={'consultor': request.user})
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Projeto criado com sucesso!')
            return redirect('core_lista_projetos_consultor')
        else:
            messages.error(request, f'Falha ao criar registro. Favor tentar novamente')
            return render(request, 'core/projeto_novo.html', data)
    else:
        return render(request, 'core/projeto_novo.html', data)


@login_required()
def projeto_update(request, id):
    data = {}
    projeto = Projeto.projetos.projeto_atual(id)
    form = ProjetoForm(request.POST or None, instance=projeto)
    data['projeto'] = projeto
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_projetos_consultor')
        else:
            return render(request, 'core/update_projeto.html', data)
    else:
        return render(request, 'core/update_projeto.html', data)


@login_required()
def projeto_delete(request, id):
    projeto = Projeto.projetos.projeto_atual(id)

    if request.method == 'POST':
        if projeto.delete():
            return redirect('core_lista_projetos_consultor')
    else:
        return render(request, 'core/delete_confirm_projeto.html', {'projeto': projeto})
