from django.urls import path

from . import views

app_name = 'cadastro_animal'

urlpatterns = [
    path("cadastro-animal/", views.cadastro, name="cadastro_animal"),
    path('animal/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal')
]