from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatusType



class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"
    model = Product
    paginate_by = 9

    def get_queryset(self):
        queryset = Product.objects.filter(
            status=ProductStatusType.publish.value
        )

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        return context




class ShopProductDetailView(DetailView):
    template_name = "shop/product-detail.html"
    def get_queryset(self):
        return Product.objects.filter(
            status=ProductStatusType.publish.value
        ).order_by('-id')
