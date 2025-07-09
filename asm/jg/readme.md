# Django
[Documentação do Django](https://docs.djangoproject.com/en/5.2/)

[HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)

- É um framework de desenvolvimento web em Python com muitos recursos prontos para uso.
- Serve como base para construir praticamente qualquer tipo de aplicação para a internet.

## Origem e Filosofia

Foi criado inicialmente para atender a sites de notícias.

**Filosofia "Baterias Inclusas"**: O Django é conhecido por vir com tudo o que é necessário para o desenvolvimento, como:

- **Django ORM**: Componente que faz a ligação com o banco de dados de forma intuitiva.
- **Sistema de Templates**: Permite criar a estrutura do HTML e conectar com os dados da aplicação.
- **Segurança**: Oferece proteção nativa contra as vulnerabilidades web mais comuns (XSS, CSRF, etc.).
- **Admin**: Interface administrativa gerada automaticamente a partir dos seus models.
- **Design Modular**: O Django é projetado em torno do conceito de "apps", módulos independentes que podem ser reutilizados em diferentes projetos.
- **Comunidade**: A comunidade em torno do Django é muito ativa e colaborativa.

## O que é um Framework?
É um "kit" de ferramentas e regras para construir um sistema sem precisar começar do zero.

- **Framework Back-end**: Focado na lógica do sistema, regras de negócio e comunicação com o banco de dados.
  - **Exemplos**: Django, Flask, FastAPI.

- **Framework Front-end**: Focado na parte visual (interface) e na interatividade com o usuário.
  - **Exemplos**: React, Angular, Vue.js.

## Arquitetura MVT (Model-View-Template)
Esta é a arquitetura de software utilizada pelo Django.

- **Model**: Representa a estrutura dos dados, geralmente mapeando uma tabela do banco de dados para uma classe Python.
- **View**: É o "cérebro" da requisição. Contém a lógica de negócio, busca dados do **Model**, processa-os e os envia para o **Template**.
- **Template**: É a camada de apresentação (geralmente um arquivo HTML) que exibe os dados para o usuário.

### Comparação com a Arquitetura MVC
O padrão MVT do Django é uma variação do conhecido padrão MVC (Model-View-Controller).

- O **Controller** do MVC é semelhante à **View** do Django (ambos cuidam da lógica da requisição).
- A **View** do MVC é semelhante ao **Template** do Django (ambos cuidam da camada de apresentação).

----

## Explicações Gerais: Estrutura do Projeto Django

- **`manage.py`**: Um script de linha de comando para interagir com seu projeto. Usado para rodar o servidor, criar apps, aplicar migrações no banco de dados, etc.

- **`myproject/`**: A pasta principal do projeto, que contém as configurações globais.

  - **`__init__.py`**: Um arquivo (geralmente vazio) que informa ao Python que este diretório deve ser considerado um "pacote", permitindo a importação de seus módulos.

  - **`settings.py`**: O coração do projeto. Contém todas as configurações:
    - Lista de `INSTALLED_APPS`.
    - Configuração do banco de dados.
    - Configuração de linguagem (`LANGUAGE_CODE`) e fuso horário (`TIME_ZONE`).
    - Definição de arquivos estáticos e de mídia.

  - **`urls.py`**: O arquivo de rotas **principal** do projeto. Ele direciona as URLs recebidas para as views correspondentes.

  - **`asgi.py`** e **`wsgi.py`**: Pontos de entrada para servidores web compatíveis com os padrões ASGI (assíncrono) e WSGI (síncrono), usados para colocar o projeto em produção.

- **`myapp/`**: Uma aplicação (módulo) do seu projeto. Apps são feitos para serem reutilizáveis.

  - **`views.py`**: Onde você escreve a lógica das suas páginas (as funções ou classes que respondem às requisições).
  - **`models.py`**: Onde você define seus modelos de dados (as classes que virarão tabelas no banco).
  - **`urls.py` (dentro do app)**: É uma boa prática criar este arquivo para gerenciar as rotas específicas deste app, mantendo o código organizado.
  - **`templates/` (dentro do app)**: Pasta para guardar os arquivos HTML (templates) relacionados a este app. Permite herança para reaproveitar estruturas como cabeçalhos e rodapés.
  - **`migrations/`**: Pasta onde o Django salva os "scripts" de alteração do banco de dados. Você não edita esses arquivos manualmente.

------

## Comandos Essenciais

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# Instalar o Django
pip install django

# Criar um novo projeto Django na pasta atual
# (O ponto '.' no final evita criar um diretório extra)
django-admin startproject myproject .

# Criar uma nova aplicação dentro do projeto
python manage.py startapp myapp

# Rodar o servidor de desenvolvimento
python manage.py runserver

# Aplicar migrações ao banco de dados (criar as tabelas iniciais)
python manage.py migrate
```