from django.shortcuts import render
import random

from django.http import HttpResponse
from django.shortcuts import render
from .forms import Choice
from pandas import DataFrame


def get_table(raw_data):
    data = []
    for i, value in enumerate(raw_data, start=1):
        data.append(
            {'Попытка': i, 'Результат': value})
    return DataFrame(data).to_html()


def flip_coin(request, tries):
    res = []
    for _ in range(tries):
        result = random.choice(['Орёл', 'Решка'])
        res.append(result)
    return render(request, 'myapp/res.html', {'res': get_table(res)})


def roll_dice(request, tries):
    res = []
    for _ in range(tries):
        result = random.randint(1, 6)
        res.append(result)
    return render(request, 'myapp/res.html', {'res': get_table(res)})


def generate_random_number(request, tries):
    res = []
    for _ in range(tries):
        result = random.randint(0, 100)
        res.append(result)
    return render(request, 'myapp/res.html', {'res': get_table(res)})


def choice_rand(request):
    if request.method == 'POST':
        form = Choice(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            tries = form.cleaned_data['tries']
            if action == 'coin':
                return flip_coin(request, tries)
            if action == 'dice':
                return roll_dice(request, tries)
            if action == 'random':
                return generate_random_number(request, tries)
    else:
        form = Choice()
    return render(request, 'myapp/index.html', {'form': form})
