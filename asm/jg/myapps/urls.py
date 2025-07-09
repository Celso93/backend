from django.urls import path
from . import views

# Boa pratica: criar esse arquivo para documentar as views
# Exemplo de acesso : http://127.0.0.0:8000/myapp/produto/1/
urlpatterns = [
    path('', views.home, name='home'),
    path('mangas', views.varios_mangas, name='mangas'),
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
    path('produto/<int:id_produto>/', views.retorne_produto, name='produto'),
]

