from django.db import models
from shared.models import TimestampMixin
import uuid

# Create your models here.
class Category(TimestampMixin):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name

class Tag(TimestampMixin):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ProductProfile(TimestampMixin):
    capacity = models.CharField(max_length=10)
    water_resistant = models.BooleanField(default=True)
    material = models.CharField(max_length=50)

    def __str__(self):
        return f"Capacity {self.capacity} Material {self.material}"
    
class Product(TimestampMixin):
    product_name =  models.CharField(max_length=100)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='product')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        null=True,
        related_name='Tags'
    )
    ProductProfile=models.ForeignKey(
        to=ProductProfile,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='ProductProfile'
    )
    warranty = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. 1 Year Warranty"
    )
    guarantee = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="e.g. 7 Days Replacement Guarantee"
    )
    cash_on_delivery = models.BooleanField(
        default=True,
        blank=True,
        null=True
    )
    stripe_product_id = models.CharField(max_length=100)
    stripe_price_id = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class ProductImage(TimestampMixin):
    product = models.ForeignKey(to=Product,on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='products/images')

    def __str__(self):
        return f"Image for {self.product.product_name}"

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(default='#FF0000')

    def __str__(self):
        return self.name

class ProductVariant(TimestampMixin):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_variants'
    )
    stock = models.PositiveIntegerField(default=0)
    color = models.ForeignKey(
        to=Color,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    size = models.CharField(
        max_length=2,
        blank=True,
        null=True,
        choices=SIZE_CHOICES
        
    )
    sku = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )
    def save(self, *args, **kwargs):
        if not self.sku:
            while True:
                sku = f"SKU-{uuid.uuid4().hex[:8].upper()}"
                if not ProductVariant.objects.filter(sku=sku).exists():
                    self.sku = sku
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.product.product_name}"


