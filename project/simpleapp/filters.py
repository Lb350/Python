from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
        conjoined=True,
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'quantity': ['gt'],
            'price': ['lt','gt'],
        }
