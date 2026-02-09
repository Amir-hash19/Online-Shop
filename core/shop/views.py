from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatusType



class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"
    model = Product
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(
            status=ProductStatusType.publish.value
        ).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context


