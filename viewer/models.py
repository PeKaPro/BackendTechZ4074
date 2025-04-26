from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)
    # description = models.TextField()
    # odebrali jsme sloupec description

    # def __repr__(self):
    #     pass

    def __str__(self) -> str:
        return f"Genre({self.name})"


class Movie(models.Model):
    title = models.CharField(max_length=128, )
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, )
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, )

    def __str__(self) -> str:
        return f"Movie({self.title})"
