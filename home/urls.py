from django.urls import path
from django.views.generic import TemplateView


from home import views
from cadastro_animal.views import lista_animais 

app_name = 'home'

urlpatterns = [
    path("", lista_animais, name="home"),
    #pagina de pesquisa do cadastro_animais
    path("pesquisar-animais/", views.pesquisar_animais, name="pesquisar_animais"),
    # URL para a página estática
    path('sobre/', TemplateView.as_view(template_name='templates_home/sobre.html'), name='sobre'),
    path('contato/', TemplateView.as_view(template_name='templates_home/contato.html'), name='contato'),
]