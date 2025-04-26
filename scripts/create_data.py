
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hollymovies.settings')

from datetime import datetime

from viewer.models import Movie, Genre

genre_names = [
    "Action", "Drama", "Sci-Fi", "Romance"
]

for name in genre_names:
    g1 = Genre(name=name)
    g1.save()



movies_data = [
    {
        "title": "Titanic",
        "genre": "Romance",
        "rating": 9,
        "released": "1990-01-01",
        "description": "Touchy movie about a sinking ship.",
    },
    {
        "title": "Avengers1",
        "genre": "Sci-Fi",
        "rating": 6,
        "released": "2010-01-01",
        "description": "Action movie about superheros",
    },
    {
        "title": "Home Alone",
        "genre": "Komedie",
        "rating": 10,
        "released": "1994-01-01",
        "description": "Burglars are wasted by 10 years old.",
    },
    {
        "title": "Shawshank redemption",
        "genre": "Drama",
        "rating": 10,
        "released": "1990-01-01",
        "description": "Escaping prison in 30 years",
    }
]


for movie_data in movies_data:
    genre_object = genres[movie_data["genre"]]
    movie = Movie(title=movie_data["title"],
                  genre=genre_object,
                  rating=movie_data["rating"],
                  released=movie_data["released"],
                  description=movie_data["description"],
                  )
    movie.save()
