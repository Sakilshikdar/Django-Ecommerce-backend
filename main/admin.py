from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.Vendor)


class ProductImagesInline(admin.StackedInline):
    model = models.ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'usd_price', 'downloads',]
    list_editable = ['usd_price']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ProductImagesInline,
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCatorgory)


class customerAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'phone']

    def get_username(self, obj):
        return obj.user.username


admin.site.register(models.Customer, customerAdmin)
admin.site.register(models.OrderItems)
admin.site.register(models.CustomerAddress)
admin.site.register(models.ProductRating)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order_time', 'order_status']


admin.site.register(models.Order, OrderAdmin)

admin.site.register(models.ProductImage)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product']


admin.site.register(models.Wishlist, WishlistAdmin)
