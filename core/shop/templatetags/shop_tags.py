from django import template
from shop.models import Product, ProductStatusType


register = template.Library()


@register.inclusion_tag("includes/latest-products.html")
def show_latest_product():
        latest_products = Product.objects.filter(
                status=ProductStatusType.publish.value).order_by("-created_date")[:8]

        
        return {"latest_products":latest_products}
    


@register.inclusion_tag("includes/similar-products.html")
def show_similar_product(product):
    similar_product = Product.objects.filter(
        status=ProductStatusType.publish.value
    ).order_by("-created_date")[:4]

    return {"similar_product": similar_product}
                
         