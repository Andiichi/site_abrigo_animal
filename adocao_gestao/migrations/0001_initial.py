# Generated by Django 4.2.16 on 2024-10-26 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro_animal', '0004_alter_galeriaanimal_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adocoes', to='cadastro_animal.cadastroanimal')),
            ],
        ),
        migrations.CreateModel(
            name='RegrasAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maior_18', models.BooleanField(default=True)),
                ('não_devolucao', models.BooleanField(default=True)),
                ('ler_contrato', models.BooleanField(default=True)),
                ('adocao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regras_adocoes', to='adocao_gestao.cadastroadocao')),
            ],
        ),
    ]