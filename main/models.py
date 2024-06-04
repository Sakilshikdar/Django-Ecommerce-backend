from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum
import datetime
# Create your models here.


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(unique=True, null=True)
    profile_img = models.ImageField(upload_to='seller_imgs/', null=True)
    address = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.user.username

    @property
    def categories(self):
        cats = Product.objects.filter(vendor=self, category__isnull=False).values(
            'category__title', 'category__id').distinct('category__title')
        return cats

    @property
    def show_chat_daily_orders(self):
        orders = OrderItems.objects.filter(product__vendor=self).values(
            'order__order_time__date').annotate(count=Count('id'))
        dateList = []
        countList = []
        dataSet = {}
        if orders:
            for order in orders:
                dateList.append(order['order__order_time__date'])
                countList.append(order['count'])
        dataSet = {'dates': dateList, 'data': countList}
        return dataSet

    @property
    def show_chat_monthly_orders(self):
        orders = OrderItems.objects.filter(product__vendor=self).values(
            'order__order_time__month').annotate(count=Count('id'))
        dateList = []
        countList = []
        dataSet = {}
        if orders:
            for order in orders:
                monthinteger = order['order__order_time__month']
                month = datetime.date(1900, monthinteger, 1).strftime('%B')
                dateList.append(month)
                countList.append(order['count'])
        dataSet = {'dates': dateList, 'data': countList}
        return dataSet

    @property
    def show_chat_yearly_orders(self):
        orders = OrderItems.objects.filter(product__vendor=self).values(
            'order__order_time__year').annotate(count=Count('id'))
        dateList = []
        countList = []
        dataSet = {}
        if orders:
            for order in orders:
                dateList.append(order['order__order_time__year'])
                countList.append(order['count'])
        dataSet = {'dates': dateList, 'data': countList}
        return dataSet

        # fetch total product
    @property
    def total_products(self):
        return Product.objects.filter(vendor=self).count()
        # dataSet = {'dates': dateList, 'data': countList}
        # return dataSet


class ProductCatorgory(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=200, null=True,default='')
    cat_img = models.ImageField(upload_to='category_imgs/', null=True)

    def __str__(self):
        return self.title

    @property
    def total_downloads(self):
        totalDownloads = 0

        products = Product.objects.filter(
            category=self)
        for product in products:
            if product.downloads:
                totalDownloads += int(product.downloads)
        return totalDownloads

    class Meta:
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCatorgory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=200, unique=True, null=True)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=200, null=True)
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
    total_amout = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_usd_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s' % (self.order_time)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    usd_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

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
