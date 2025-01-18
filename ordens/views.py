from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import OrdemServico
from .forms import OrdemServicoForm
from django.shortcuts import get_object_or_404
from django.contrib import messages 


def pagina_inicial(request):
    return HttpResponse("Página Inicial de Ordens de Serviço")

def listar_ordens(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'ordens/listagem.html', {'ordens': ordens})

def cadastrar_ordem(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ordem de serviço cadastrada com sucesso!")
            return redirect('ordens:listar')
    else:
        form = OrdemServicoForm()
    return render(request, 'ordens/cadastro.html', {'form': form})

def editar_ordem(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST, instance=ordem)
        if form.is_valid():
            form.save()
            messages.success(request, "Ordem de serviço editada com sucesso!")
            return redirect('ordens:listar')
    else:
        form = OrdemServicoForm(instance=ordem)
    return render(request, 'ordens/editar.html', {'form': form, 'ordem': ordem})

def excluir_ordem(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        ordem.delete()
        messages.success(request, "Ordem de serviço excluída com sucesso!")
        return redirect('ordens:listar')
    return render(request, 'ordens/excluir.html', {'ordem': ordem})

def gerar_relatorio(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        ordem.delete()
        messages.success(request, "Ordem de serviço excluída com sucesso!")
        return redirect('ordens:listar')
    return render(request, 'ordens/excluir.html', {'ordem': ordem})
