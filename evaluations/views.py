from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import Projeto
from .models import Avaliacao
from .forms import AvaliacaoForm


@login_required()
def lista_avaliacoes_consultor(request):
    avaliacoes = Avaliacao.avaliacoes.avaliacoes_usuario(request.user)
    return render(request, 'evaluations/lista_avaliacoes_consultor.html', {'avaliacoes': avaliacoes})


@login_required()
def avaliacao_detail(request, id):
    avaliacao = Avaliacao.avaliacoes.avaliacao_atual(id)
    return render(request, 'evaluations/avaliacao_detail.html', {'avaliacao': avaliacao})


@login_required()
def avaliacao_novo(request):
    data = {}

    form = AvaliacaoForm(request.POST or None, initial={'avaliador': request.user})
    data['form'] = form
    form.fields["avaliador"].disabled = True
    form.fields["projeto"].queryset = Projeto.projetos.projetos_usuario(request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Avaliação registrada!')
            return redirect('evaluations_lista_avaliacoes_consultor')
        else:
            messages.error(request, f'Falha ao criar registro. Favor tentar novamente')
            return render(request, 'evaluations/avaliacao_novo.html', data)
    else:
        return render(request, 'evaluations/avaliacao_novo.html', data)


@login_required()
def avaliacao_update(request, id):
    data = {}
    avaliacao = Avaliacao.avaliacoes.avaliacao_atual(id)
    form = AvaliacaoForm(request.POST or None, instance=avaliacao,
                         initial={'projeto': avaliacao.projeto, 'avaliador': request.user})
    data['avaliacao'] = avaliacao
    data['form'] = form

    form.fields['projeto'].disabled = True
    form.fields['avaliador'].disabled = True


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('evaluations_lista_avaliacoes_consultor')
        else:
            return render(request, 'evaluations/update_avaliacao.html', data)
    else:
        return render(request, 'evaluations/update_avaliacao.html', data)


@login_required()
def avaliacao_delete(request, id):
    avaliacao = Avaliacao.avaliacoes.avaliacao_atual(id)

    if request.method == 'POST':
        if avaliacao.delete():
            return redirect('evaluations_lista_avaliacoes_consultor')
    else:
        return render(request, 'evaluations/delete_confirm_avaliacao.html', {'avaliacao': avaliacao})
