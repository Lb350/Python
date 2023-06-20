from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    # queryset = Product.objects.filter(
    #     price__lt=300
    # )
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Распродажа в среду!"
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'