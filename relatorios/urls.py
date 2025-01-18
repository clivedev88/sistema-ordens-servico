from django.urls import path
from . import views

app_name = 'relatorios'

urlpatterns = [
    path('gerar/', views.gerar_relatorio, name='gerar'),
]
