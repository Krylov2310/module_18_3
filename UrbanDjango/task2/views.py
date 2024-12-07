from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def info(request):
    return render(request, 'second_task/info.html')


def index(request):
    return render(request, 'second_task/index.html')


class index2(TemplateView):
    template_name = 'second_task/index2.html'