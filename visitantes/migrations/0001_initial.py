# Generated by Django 3.0 on 2021-03-10 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Numero da Casa a Ser Visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do Veículo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de Chegada na Portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horário de Saída do Condomínio')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horário de Autorização de Entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nomde do Morador Responsável por Autorizar a Entrada do Visitante')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.Porteiro', verbose_name='Porteiro Responsável pelo Registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]