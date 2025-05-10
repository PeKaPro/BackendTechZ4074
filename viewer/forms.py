
import re
from datetime import date

import django.forms as forms
from django.core.exceptions import ValidationError

from viewer.models import Genre, Movie


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Prvni pismeno by melo byt velke.")


class PastMonthDateField(forms.DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError("Pouze data z minulosti jsou povolena.")

    def clean(self, value):
        result = super().clean(value)
        return date(result.year, result.month, 1)


class MovieForm(forms.Form):
    title = forms.CharField(max_length=128, validators=[capitalized_validator])
    genre = forms.ModelChoiceField(queryset=Genre.objects)
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthDateField()
    description = forms.CharField(widget=forms.Textarea)

    # clean_NAZEV_POLE
    def clean_description(self):
        description = self.cleaned_data["description"]
        description_sentences = re.sub(r"\s*\.\s*",".", description).split(".")
        clean = ". ".join([sentence.capitalize() for sentence in description_sentences]) + "."
        return clean

    def clean(self):
        result = super().clean()
        if result["genre"].name.lower() == "sci-fi".lower() and result["released"].year < 1970:
            raise ValidationError("Takhle stare scifi nemohou existovat...")
        return result


class MovieForm2(forms.ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"

        # fields = ["title", "genre", "rating", "released", "description"]
        # ignore = ["title"]

    title = forms.CharField(max_length=128, validators=[capitalized_validator])
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthDateField()

    # clean_NAZEV_POLE
    def clean_description(self):
        description = self.cleaned_data["description"]
        description_sentences = re.sub(r"\s*\.\s*",".", description).split(".")
        clean = ". ".join([sentence.capitalize() for sentence in description_sentences]) + "."
        return clean

    def clean(self):
        result = super().clean()
        if result["genre"].name.lower() == "sci-fi".lower() and result["released"].year < 1970:
            raise ValidationError("Takhle stare scifi nemohou existovat...")
        return result


class MovieFormCustom(forms.ModelForm):

    class Meta:
        model = Movie
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
