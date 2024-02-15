from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.user.username


class ProductCatorgory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        ProductCatorgory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    details = models.CharField(null=True)
    tags = models.TextField(null=True)
    price = models.FloatField()

    def tags_list(self):
        tagList = self.tags.split(',')
        return tagList

    def __str__(self):
        return self.title


class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phome = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


# customer address
class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address


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
