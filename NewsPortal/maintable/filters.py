from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms

class PostFilter(FilterSet):
    time_in = DateFilter(
        field_name='time_in',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата',
        lookup_expr='date__gte'
    )
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            # 'time_in': ['gt'],
        }
