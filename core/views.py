from django.shortcuts import render
from random import randint
from django.http import HttpResponse

def home(request):
    # contexto = {'dados': num }
    games = []
    while len(games) < 11:
        list = []

        while len(list) < 6:
            num = randint(0, 60)
            if num not in list:
                list.append(num)

        list.sort()

        if list not in games:
            games.append(list)

    html = f'<body> ' \
                f'<p>Simulador de Loteria</p>' \
                    '{% for i in loteria %}' \
                        'jogo = {{i}}' \
                    '{% endfor%}'\
           f'<p></p>' \
           f'Jogo = {games}</body>'

    return HttpResponse(html)