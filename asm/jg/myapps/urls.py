from django.urls import path
from . import views

# boa pratica de criar esse arquivo para documentar as views
# exemplo de acesso : http://127.0.0.0:8000/myapp/produto/1/
urlpatterns = [
    path('', views.home, name='home'),
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
    path('produto/<int:id_produto>/', views.retorne_produto, name='produto'),
]

