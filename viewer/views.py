# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView

from viewer.forms import MovieForm, MovieForm2, MovieFormCustom
from viewer.models import Movie



def hello(request):
    return HttpResponse('Hello World!')


def hello2(request, s):
    return HttpResponse(f'Hello {s} World!')


"""
http://centrum.cz/neco/neco_dalsiho?key1=value1&key2=value2
http://centrum.cz/neco/neco_dalsiho?s=123

"""


def hello3(request):
    s = request.GET.get('s', "Default")
    return HttpResponse(f'Hello {s} World!')


def hello4(request, s0):
    s1 = request.GET.get('s1', '')

    data =  [s0, s1, 'beautiful', 'wonderful']
    # data = [slovo.upper() for slovo in data]

    return render(
        request,
        template_name='hello.html',
        context={'adjectives': data}
    )


def hello5(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name='hello_with_base.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


@login_required
def movies(request):
    all_movies = Movie.objects.all()
    template_name = 'movies1.html'
    return render(
        request, template_name, {'movies': all_movies}
    )


class MoviesView1(LoginRequiredMixin, View):
    def get(self, request):
        all_movies = Movie.objects.all().order_by("rating")
        template_name = 'movies1.html'
        return render(
            request, template_name, {'movies': all_movies}
        )


class MoviesView2(LoginRequiredMixin, TemplateView):
    template_name = 'movies1.html'
    extra_context = {"movies": Movie.objects.all().order_by("-rating")}


class MoviesView3(LoginRequiredMixin, ListView):
    template_name = 'movies2.html'
    model = Movie


class MovieCreateView(FormView):
    template_name = 'movies_form.html'
    form_class = MovieForm
    success_url = reverse_lazy("moje_filmy")

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data

        Movie.objects.create(
            title=cleaned_data["title"],
            genre=cleaned_data["genre"],
            rating=cleaned_data["rating"],
            released=cleaned_data["released"],
            description=cleaned_data["description"],
        )
        return result

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class MovieCreateView2(CreateView):
    template_name = 'movies_form.html'
    form_class = MovieForm2
    model = Movie
    success_url = reverse_lazy("moje_filmy")


class MovieUpdateView(UpdateView):
    template_name = "movies_form.html"
    model = Movie
    form_class = MovieForm2
    success_url = reverse_lazy("moje_filmy")


class MovieDeleteView(DeleteView):
    template_name = "movies_delete.html"
    model = Movie
    success_url = reverse_lazy("moje_filmy")



class MovieCreateCustomView(FormView):
    template_name = 'movies_form_nice.html'
    form_class = MovieFormCustom
    success_url = reverse_lazy("moje_filmy")

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data

        Movie.objects.create(
            title=cleaned_data["title"],
            genre=cleaned_data["genre"],
            rating=cleaned_data["rating"],
            released=cleaned_data["released"],
            description=cleaned_data["description"],
        )
        return result

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
