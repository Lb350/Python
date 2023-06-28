from django.urls import path
from .views import ProductsList, ProductDetail, create_product


urlpatterns = [
    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
    path('create/', create_product, name='product_create'),
]