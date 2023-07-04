from django import forms
import django_filters
from .models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(min_length=3)

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'time_in',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        time_in = cleaned_data.get('time_in')