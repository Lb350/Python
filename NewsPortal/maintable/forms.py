from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'category',
            'text_post',

        ]
        widgets = {'category': CheckboxSelectMultiple}
        # type_paper = 'NWS'

