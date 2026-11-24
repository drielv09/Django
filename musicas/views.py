from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MusicaForm
from .models import Musica

def lista(request): 
    musicas = Musica.objects.all()
    return render(request, 'musicas/lista.html', {'musicas':musicas})

def criar(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Música adicionada!')
            return redirect('lista')
    else:
        form = MusicaForm()
    return render(request, 'musicas/form.html', {'form': form, 'titulo_pagina': 'Nova música'})

def editar(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            messages.success(request, 'Música atualizada!')
            return redirect('lista')
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'musicas/form.html', {'form': form, 'titulo_pagina': 'Editar música'})

def excluir(request, id):
    musica = get_object_or_404(Musica, id=id)
    if request.method == 'POST':
        musica.delete()
        messages.success(request, 'Música excluída!')
        return redirect('lista')
    return render(request, 'musicas/confirmar_exclusao.html', {'musica': musica})