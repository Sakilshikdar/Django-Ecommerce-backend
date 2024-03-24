from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(unique=True, null=True)
    profile_img = models.ImageField(upload_to='seller_imgs/', null=True)
    address = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.user.username


class ProductCatorgory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCatorgory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=200, unique=True, null=True)
    title = models.CharField(max_length=200)
    details = models.CharField(null=True)
    tags = models.TextField(null=True)
    # price = models.FloatField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2)
    usd_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=100)
    demo_url = models.URLField(null=True, blank=True)
    image = models.ImageField(
        upload_to='product_imgs/', null=True, blank=True)
    product_file = models.FileField(upload_to='product_files/', null=True)
    downloads = models.CharField(max_length=100, default=0, null=True)
    publish_status = models.BooleanField(default=False)

    def tags_list(self):
        if self.tags:
            tagList = self.tags.split(',')
            return tagList

    def __str__(self):
        return self.title


class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(unique=True, null=True)
    profile_img = models.ImageField(upload_to='customer_imgs/', null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_orders')
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    total_use_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s' % (self.order_time)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = 'Order Items'


# customer address
class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Customer Address'


# product review and rating

class ProductRating(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_ratings')
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='rating_customers')
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.reviews}'


# product images
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_imgs')
    image = models.ImageField(upload_to='product_imgs/', null=True, blank=True)

    def __str__(self):
        return self.image.url


# Whislist Model
class Wishlist (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Wish list'

    def __str__(self):
        return f"{self.product.title} - {self.customer.user.first_name}"
