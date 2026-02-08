from django.db import models



class ProductStatusType(models.IntegerChoices):
    publish = 1
    draft = 2 



class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    created_date = models.DateTimeField(auto_now_add=False)
    updated_date = models.DateTimeField(auto_now=False)



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
    created_date = models.DateTimeField(auto_now_add=False)
    updated_date = models.DateTimeField(auto_now=False)



class ProductImage(models.Model):
    product = models.ForeignKey("account.User", on_delete=models.CASCADE)
    file = models.ImageField(upload_to="product/extra-img/")
    created_date = models.DateTimeField(auto_now_add=False)
    updated_date = models.DateTimeField(auto_now=False)
