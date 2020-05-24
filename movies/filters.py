from django import forms
from .models import Movie
import django_filters


class MovieFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    genre = django_filters.CharFilter(
        widget=forms.Select(choices=(('', '請選擇'),) + Movie.GENRE_CHOICES, attrs={'class': 'form-control'}))

    release_year = django_filters.CharFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Movie
        fields = '__all__'
