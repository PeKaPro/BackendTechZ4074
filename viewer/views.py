
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from viewer.forms import MovieForm
from viewer.models import Movie


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
        request,
        template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def hello5(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name='hello_with_base.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def movies(request):
    all_movies = Movie.objects.all().order_by("rating")
    template_name = 'movies1.html'
    return render(
        request, template_name, {'movies': all_movies}
    )


class MoviesView1(View):
    def get(self, request):
        all_movies = Movie.objects.all().order_by("rating")
        template_name = 'movies1.html'
        return render(
            request, template_name, {'movies': all_movies}
        )


class MoviesView2(TemplateView):
    template_name = 'movies1.html'
    extra_context = {"movies": Movie.objects.all().order_by("-rating")}


class MoviesView3(ListView):
    template_name = 'movies2.html'
    model = Movie


class MovieCreateView(FormView):
    template_name = 'movies_create.html'
    form_class = MovieForm
    success_url = reverse_lazy("index")

