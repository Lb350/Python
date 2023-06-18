from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'default.html'
    context_object_name = 'products'
