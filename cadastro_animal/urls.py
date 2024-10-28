from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro-animal/", views.cadastro, name="cadastro_animal"),
    path("lista-animais/", views.lista_animais, name="lista_animais"),
    path('animal/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal')
]