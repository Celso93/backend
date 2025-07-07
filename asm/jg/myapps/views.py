from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# view 'e uma funcao python
# toda view, em teoria, recebe uma request
def home(request):
    hora_atual = datetime.now().hour

    if 0 >= hora_atual < 12:
        # maneira de verificar valor entre valores
        texto = 'Bom dia'
    elif 12 >=  hora_atual < 18:
        texto = 'Boa tarde'
    else:
        texto = 'Boa noite'

    return HttpResponse(f'{texto} ! Ola mundo')
    # criacada a view, configurar em urls

# Exemplo de view com um parametro
def saudacao(request, nome):
    return HttpResponse(f'Ola {nome}, seja bem vindo')

# varios parametros
# exemplo requisicao no banco
def retorne_produto(request, id_produto):
    produtos = {
        1:"PC gamer",
        2:"Notebook",
        3:"Leptop da xuxa",
    }

    produto = produtos.get(id_produto, "Produtos nao encontrados")

    return HttpResponse(f'Detalhes do produto: {produto}')