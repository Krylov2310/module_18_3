from django.shortcuts import render


menu_ = {'Главная': ["http://127.0.0.1:8000/"], 'Магазин': ["http://127.0.0.1:8000/games/"],
         'Корзина': ["http://127.0.0.1:8000/cart/"]}


# Create your views here.
def platform(request):
    pagename = 'Главная страница'
    menu = menu_
    context = {
        'pagename': pagename,
        'menu': menu,
    }
    return render(request, 'third_task/platform.html', context)


def games(request):
    pagename = 'Игры'

    content = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"],
               'programs': ["Microsoft Office", "Windows 10 Pro"]}
    context = {
        'pagename': pagename,
        'menu': menu_,
        'content': content
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    pagename = 'Корзина'
    menu = menu_
    content = 'Извините, ваша корзина пуста'
    context = {
        'pagename': pagename,
        'menu': menu,
        'content': content
    }
    return render(request, 'third_task/cart.html', context)