from django.shortcuts import render
from random import randint

def home(request):
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

    contexto = {'lottery': games }

    return render(request, 'index.html', contexto)