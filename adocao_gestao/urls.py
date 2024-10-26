from django.urls import path

from . import views

app_name = 'adocao_gestao'

urlpatterns = [
    path("cadastro/adocao/", views.cadastro_adocao, name="adote"),
]