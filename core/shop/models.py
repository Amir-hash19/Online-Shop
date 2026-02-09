from django.db import models
from decimal import Decimal


class ProductStatusType(models.IntegerChoices):
    publish = 1
    draft = 2 



class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.created_date}"



class Product(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategory)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(default="/default/product-image.png", upload_to="product/img/")
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]



    def get_price(self):        
        discount_amount = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_amount
        return round(discounted_amount)


    def __str__(self):
        return f"{self.title} {self.created_date}"
    



class ProductImage(models.Model):
    product = models.ForeignKey("account.User", on_delete=models.CASCADE)
    file = models.ImageField(upload_to="product/extra-img/")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
