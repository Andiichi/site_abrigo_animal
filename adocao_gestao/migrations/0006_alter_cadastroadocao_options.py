# Generated by Django 4.2.16 on 2024-10-27 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adocao_gestao', '0005_alter_regrasadocao_solicitacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastroadocao',
            options={'ordering': ['-nome'], 'verbose_name': 'Cadastro de Adoção', 'verbose_name_plural': 'Cadastro de Adoções'},
        ),
    ]
