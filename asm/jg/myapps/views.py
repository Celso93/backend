from django.shortcuts import render
from django.http import HttpResponse
from .utils import time

# View e uma funcao python
# Toda view, em teoria, recebe uma request
def home(request):
    dados = {
        'exemplo1': 'Teste de dado dinamico',
        'exemplo2': 'Exemplo2',
        'saudacao': time.msg_saudacao(),
    }
    
    # Renderizando html
    return render(request, 'home.html', {
        'saudacao': dados['saudacao'],  
        'dado': dados['exemplo1'],
        'outro_dado': dados['exemplo2']
    })

# View com um parametro
def saudacao(request, nome):
    return HttpResponse(f'Ola {nome}, seja bem vindo')

# Varios parametros (Exemplo requisicao no banco)
def retorne_produto(request, id_produto):
    produtos = {
        1:"PC gamer",
        2:"Notebook",
        3:"Leptop da xuxa",
    }

    produto = produtos.get(id_produto, "Produtos nao encontrados")

    return HttpResponse(f'Detalhes do produto: {produto}')

# exemplo de for
def varios_mangas(request):
    mangas = ["One piece", "Hunter x Hunter", "Demon Slayer"]

    return render(request, 'mangas.html', {'mangas': mangas})