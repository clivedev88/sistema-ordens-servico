from django.urls import path
from . import views

app_name = 'ordens'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listagem/', views.listar_ordens, name='listar'),
    path('cadastro/', views.cadastrar_ordem, name='cadastro'), 
    path('editar/<int:pk>/', views.editar_ordem, name='editar'),
    path('excluir/<int:pk>/', views.excluir_ordem, name='excluir'),
    path('relatorios/', views.gerar_relatorio, name='relatorio'),
]
