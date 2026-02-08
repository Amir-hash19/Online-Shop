from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatusType

class ShopProductGridView(TemplateView):
    template_name = "shop/product-grid.html"
    queryset = Product.objects.filter(status=ProductStatusType.publish.value)
