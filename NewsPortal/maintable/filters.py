from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms
from django import template

register = template.Library


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

forbidden_words = []
@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + '*'*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return ' '.join(result)