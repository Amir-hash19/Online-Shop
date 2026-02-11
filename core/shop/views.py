from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatusType, ProductCategory
from django.core.exceptions import FieldError


class ShopProductGridView(ListView):
    template_name = "shop/product-grid.html"
    model = Product
    paginate_by = 9

    def get_paginate_by(self, queryset):
        return self.request.GET.get("page_size", self.paginate_by)

    def get_queryset(self):
        queryset = Product.objects.filter(
            status=ProductStatusType.publish.value
        )

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)

        category_id = self.request.GET.get("category_id")

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if min_price:= self.request.GET.get("min_price"):
            queryset = queryset.filter(price__gte=min_price)    

        if max_price:= self.request.GET.get("max_price"):
            queryset = queryset.filter(price__lte=max_price)   

        if order_by := self.request.GET.get("order_by"):
                try:
                    queryset = queryset.order_by(order_by)
                except FieldError:
                    pass    
                    
        return queryset    



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_items"] = self.get_queryset().count()
        context["categories"] = ProductCategory.objects.all()
        return context




class ShopProductDetailView(DetailView):
    template_name = "shop/product-detail.html"
    def get_queryset(self):
        return Product.objects.filter(
            status=ProductStatusType.publish.value
        ).order_by('-id')
