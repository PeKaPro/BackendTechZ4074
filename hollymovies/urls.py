"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import hello, hello2, hello3, hello4, hello5, movies, MoviesView1, MoviesView2, MoviesView3, MovieCreateView

from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', hello),
    path('hello2/<s>', hello2),
    path('ahoj', hello3),
    path("hello4/<s0>", hello4),
    path("hello5/<s0>", hello5),
    path("moje_filmy/moje_filmy/moje_filmy", movies, name="index"),
    path("movies_cbv1", MoviesView1.as_view()),
    path("movies_cbv2", MoviesView2.as_view()),
    path("movies_cbv3", MoviesView3.as_view()),

    path("movie/create", MovieCreateView.as_view()),
]

