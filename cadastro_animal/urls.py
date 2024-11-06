from django.urls import path

from . import views

urlpatterns = [
    path("cadastro-animal/", views.cadastro, name="cadastro_animal"),
    path("", views.lista_animais, name="home"),
    path('animal/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal')
]