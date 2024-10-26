from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro_animal/", views.cadastro, name="cadastro_animal"),
    path("lista_animais/", views.lista_animais, name="lista_animais"),
    path('animal/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal'),
    path("pesquisar_animais/", views.pesquisar_animais, name="pesquisar_animais")
]