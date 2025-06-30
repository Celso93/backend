'''
Crie um jogo dos estados.
Neste jogo, o jogador precisa responder o nome da capital de cada Estado do Brasil.
O jogo deve perguntar ao usuario "Qual a capital do estado X?".
e checar se o usuario respondeu de forma correta.
Apos cada pergunta, o usuario pode escolher para o jogo ou continuar para a proxima pergunta.
Quando o usuario decidi para, ou quando todas as perguntas foram respondidas,
O codigo mostra o numero bruto de acertos.

Decompondo
1. preciso de um dicionario dos estados x capitais e o numero de acertos
2. iteragir com as minhas capitas em ordem alfabetica ? 
3. devo pegar um input e verificar se a resposta esta correta
    3.1 Caso correto: dar outro input para saber se vai continuar ou parar
    3.2 Caso errado : avisar que errou e continuar
4. Caso pare ou finalize apresentar o numero de acertos
'''
acertos = 0

capitais_brasil_sem_acentos = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceio',
    'Amapa': 'Macapa',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceara': 'Fortaleza',
    'Distrito Federal': 'Brasilia',
    'Espirito Santo': 'Vitoria',
    'Goias': 'Goiania',
    'Maranhao': 'Sao Luis',
    'Mato Grosso': 'Cuiaba',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Para': 'Belem',
    'Paraiba': 'Joao Pessoa',
    'Parana': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piaui': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondonia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianopolis',
    'Sao Paulo': 'Sao Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}


print("--- Jogo das Capitais do Brasil ---")

for estado, capital_correta in capitais_brasil_sem_acentos.items():
    resposta_usuario = input(f"Qual a capital do estado {estado}? ")
    
    if resposta_usuario.upper() == capital_correta.upper():
        print("Resposta Correta!")
        acertos += 1
    else:
        print(f"Resposta Errada! :( A capital correta é {capital_correta.upper()}.")
    
    while True:
        continuar = input("Digite 'continuar' para a próxima pergunta ou 'parar' para sair: ").lower()
        if continuar in ('continuar', 'parar'):
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    if continuar == 'parar':
        break

print(f"Sua pontuação final foi: {acertos} acertos.")
