from django.urls import path

from . import views

app_name = 'adocao_gestao'

urlpatterns = [
    path("cadastro-adocao/", views.cadastro_adocao, name="adote"),
    path('aprovar-adocao/<int:adocao_id>/', views.aprovar_desaprovar_adocao, name='aprovar_desaprovar_adocao'),
    path('lista-adocoes/', views.lista_adocoes, name='lista_adocoes'),
]