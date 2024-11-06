from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'home'

urlpatterns = [
    path("", views.lista_animais, name="home"),
    #pagina de pesquisa do cadastro_animais
    path("pesquisar-animais/", pesquisar_animais, name="pesquisar_animais"),
    # URL para a página estática
    path('sobre/', TemplateView.as_view(template_name='sobre.html'), name='sobre'),
    path('contato/', TemplateView.as_view(template_name='contato.html'), name='contato'),
]