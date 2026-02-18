from django import template
from shop.models import Product, ProductStatusType


register = template.Library()


@register.inclusion_tag("includes/latest-products.html")
def show_latest_product():
        latest_products = Product.objects.filter(
                status=ProductStatusType.publish.value).order_by("-created_date")[:8]

        
        return {"latest_products":latest_products}
    

    