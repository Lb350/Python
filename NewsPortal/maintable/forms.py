from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'text_post',
            'connect_categories',

        ]
        # type_paper = 'NWS'

