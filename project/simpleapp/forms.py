from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=10)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')

        if name == description:
            raise ValidationError('Описание не должно быть идентично названию.')
        return cleaned_data