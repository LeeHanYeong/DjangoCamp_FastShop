from django.views.generic import DetailView

from product.models import Product


class ProductDetail(DetailView):
    model = Product
