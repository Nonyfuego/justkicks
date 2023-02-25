from django.db import models

# Create your models here.
class Product(models.Model):
    COLORS = [
        ('red','RED'),
        ('black','BLACK'),
        ('white','WHITE'),
        ('blue','BLUE'),
        ('brown', 'BROWN'),
        ('gray','GRAY')
    ]
    SIZES = [
        ('38','38'),
        ('39','39'),
        ('40','40'),
        ('41','41'),
        ('42','42'),
        ('43','43'),
        ('44','44'),
        ('45','45'),
        ('46','46')
    ]
    name = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand',on_delete=models.CASCADE)
    color = models.CharField(max_length=50,choices=COLORS)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/')
    size = models.CharField(max_length=2, choices=SIZES)
    footware_type = models.ForeignKey('FootwearType', on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    price = models.FloatField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    TITLES = [
        ('men', 'MEN'),
        ('women', 'WOMEN'),
        ('kids', 'KIDS'),
    ]
    title = models.CharField(max_length=50,choices=TITLES)

    def __str__(self) -> str:
        return self.title


class FootwearType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="brand_photos/")

    @property
    def products(self):
        products = []
        all_products = Product.objects.all()
        for product in all_products:
            if product.brand.name == self.name:
                products.append(product)
        return products

    def __str__(self) -> str:
        return self.name