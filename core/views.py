from django.shortcuts import render
from random import randint
from django.http import HttpResponse

def home(request):
    num = randint(0, 60)
    # contexto = {'dados': num }
    html = f'<body> Número gerado = {num} </body>'
    return HttpResponse(html)