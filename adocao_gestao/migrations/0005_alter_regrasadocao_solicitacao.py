# Generated by Django 4.2.16 on 2024-10-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adocao_gestao', '0004_alter_regrasadocao_solicitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regrasadocao',
            name='solicitacao',
            field=models.CharField(choices=[('feito', 'Em analise'), ('concluido', 'Adoção aprovada'), ('cancelado', 'Adoção reprovada')], default='feito', max_length=10),
        ),
    ]