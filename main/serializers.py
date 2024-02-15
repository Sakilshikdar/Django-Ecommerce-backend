from rest_framework import serializers
from .models import Vendor, ProductCatorgory, Product, Customer, Order, OrderItem, CustomerAddress, ProductRating, ProductImage


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']

        def __init__(self, *args, **kwargs):
            super(VendorSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address']

        def __init__(self, *args, **kwargs):
            super(VendorSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1

# product image serializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductrListSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title',
                  'product_ratings', 'tags_list', 'details', 'price']

        def __init__(self, *args, **kwargs):
            super(ProductrListSerializer, self).__init__(*args, **kwargs)

            # self.Meta.depth = 1


class PeoductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)
    product_imgs = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title',
                  'product_ratings', 'product_imgs', 'tags_list', 'details', 'price']

        def __init__(self, *args, **kwargs):
            super(ProductrListSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'phome']

        def __init__(self, *args, **kwargs):
            super(CustomerSerializer, self).__init__(*args, **kwargs)


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'phome']

        def __init__(self, *args, **kwargs):
            super(CustomerDetailSerializer, self).__init__(*args, **kwargs)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer']

        def __init__(self, *args, **kwargs):
            super(OrderSerializer, self).__init__(*args, **kwargs)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product']

        def __init__(self, *args, **kwargs):
            super(OrderDetailSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


# customer addres
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ['id', 'customer', 'address', 'default_address']

        def __init__(self, *args, **kwargs):
            super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


# ratting and review

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = ['id', 'customer', 'product', 'rating', 'reviews', 'add_time']

        def __init__(self, *args, **kwargs):
            super(ProductRatingSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


# category serializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatorgory
        fields = ['id', 'title', 'detail']

        def __init__(self, *args, **kwargs):
            super(CategorySerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


class CategoryeDtailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCatorgory
        fields = ['id', 'title', 'detail']

        def __init__(self, *args, **kwargs):
            super(CategoryeDtailSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1
