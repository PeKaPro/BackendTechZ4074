

import django.forms as forms

from viewer.models import Genre


class MovieForm(forms.Form):
    title = forms.CharField(max_length=128)
    genre = forms.ModelChoiceField(queryset=Genre.objects)
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = forms.DateField()
    description = forms.CharField(widget=forms.Textarea)

