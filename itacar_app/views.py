from datetime import datetime  #biblioteca python para trabalhar com datas
import random #biblioteca python para gerar numeros aleatorios
from http import client #biblioteca python para fazer conexão com um nó cliente. Esse nó seria o navegador do usuário final do nosso sistema
from django.shortcuts import render #biblioteca do django para enviar respostas usando o protocolo http
from django.shortcuts import redirect #biblioteca do django para redirecionar de uma interface web (página web) para outra - cria a navegação entre páginas web
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def home(request):
    #método executado quando o usuário está na interface (paǵina html) inicial do sistema  home.html
    return render(request, "ita_car/home.html")

def efetuarLogin(request):
    return render(request, "ita_car/efetuarLogin.html")

def historicoCorrida(request):
    return render(request, "ita_car/historicoCorrida.html")