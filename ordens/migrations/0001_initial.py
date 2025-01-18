# Generated by Django 5.1.5 on 2025-01-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')], default='pendente', max_length=20)),
            ],
        ),
    ]
