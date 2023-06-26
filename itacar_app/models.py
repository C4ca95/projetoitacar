from distutils.archive_util import make_zipfile
from xml.parsers.expat import model
# biblioteca do Django para trabalhar com o banco de dados
from django.db import models
from django.forms import CharField, Field
from django.utils import timezone
import datetime
from django.conf import settings

import os

# Obtenha o caminho absoluto para o arquivo de configuração do Django
django_settings_module = os.path.abspath(os.path.join(os.path.dirname(__file__), 'itacar_app', 'settings.py'))

# Defina o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ita_car_app.settings')

class motorista(models.Model):
    nomeMotorista = models.CharField(max_length=100)
    nomeDoCarro = models.CharField(max_length=100)
    placaDoCarro = models.CharField(max_length=100)
    classificacaoEstrelas = models.IntegerField()
    IDMotorista = models.IntegerField()
    CPF = models.IntegerField()

def registrarMotorista(self):
    # O DJANGO RECONHECE A TABELA NO BANCO DE DADOS
    self.save()

def classificacaoEstrelas(self, classificacaoEstrelas):
    classificacaoEstrelas = 0

    novaAval = input('Quantas estrelas o motorista merece?')

    classificacaoEstrelas = novaAval

    if classificacaoEstrelas == 1:
        print('O número de estrelas desse motorista é de 1 estrela')
    elif classificacaoEstrelas == 2:
        print('O número de estrelas desse motorista é de 2 estrelas')
    elif classificacaoEstrelas == 3:
        print('O número de estrelas desse motorista é de 3 estrelas')
    elif classificacaoEstrelas == 4:
        print('O número de estrelas desse motorista é de 4 estrelas')
    elif classificacaoEstrelas == 5:
        print('O número de estrelas desse motorista é de 5 estrelas')
    else:
        print('O número de estrelas deve ser compreendido entre 1 e 5')

    print(classificacaoEstrelas)

class relatorioFinanceiro(models.Model):
    IDMotorista = models.IntegerField()
    qtdRecebimento = models.IntegerField()
    data = models.DateField()
    somatotal = models.FloatField()
    CPF = models.IntegerField()

def valorTotalRecebido(self, somatotal, qtdRecebimento):
    somatotal = []

    qtdRecebimento = input('Digite a quantidade recebida pela corrida: ')

    if qtdRecebimento > 0:
        qtdRecebimento = somatotal
    else:
        print("O valor deve ser maior que 0 reais")

class HistoricoViagem(models.Model):
    IDMotorista = models.IntegerField()
    IDpassageiro = models.IntegerField()
    data = models.DateField()
    horario = models.DateTimeField()
    valorViagem = models.FloatField()

def mostrarHistorico(self):
    # Banco de dados terá as viagens e o Django já o reconhece
    self.save()

