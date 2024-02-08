from django.shortcuts import render


def index(reqest):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'hello', '123'],
    }
    return render(reqest, 'main/index.html', data)


def about(reqest):
    return render(reqest, 'main/about.html')
