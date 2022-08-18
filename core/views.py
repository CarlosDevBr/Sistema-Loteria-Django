from django.shortcuts import render
from random import randint

def home(request):
    n = 0
    if request.POST:
        n = int(request.POST['valor'])
    games = []
    while len(games) < n:
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