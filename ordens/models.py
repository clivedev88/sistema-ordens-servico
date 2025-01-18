from django.db import models
from django.contrib.auth.models import User

class OrdemServico(models.Model):
    cliente = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('concluido', 'Concluído'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendente'
    )

    def __str__(self):
        return f"{self.cliente} - {self.status}"