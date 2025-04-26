
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('Hello World!')


def hello2(request, s):
    return HttpResponse(f'Hello {s} World!')


def hello3(request):
    s = request.GET.get('s', "Default")
    return HttpResponse(f'Hello {s} World!')


def hello4(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )
