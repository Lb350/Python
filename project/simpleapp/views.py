from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    # queryset = Product.objects.filter(
    #     price__lt=300
    # )
    template_name = 'products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'