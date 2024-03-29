from rest_framework import serializers
from .models import Vendor, ProductCatorgory, Product, Customer, Order, OrderItems, CustomerAddress, ProductRating, ProductImage, Wishlist
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',  'email']


class VendorSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response

    class Meta:
        model = Vendor
        fields = ['id', 'user', 'address', 'profile_img', 'phone']

        def __init__(self, *args, **kwargs):
            super(VendorSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response

    class Meta:
        model = Vendor
        fields = ['id', 'user', 'profile_img', 'phone', 'address', 'show_chat_daily_orders',
                  'show_chat_monthly_orders', 'show_chat_yearly_orders', 'total_products']

        def __init__(self, *args, **kwargs):
            super(VendorDetailSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


# product image serializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class ProductrListSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)

    product_imgs = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'image', 'title', 'tags', 'publish_status', 'slug',
                  'product_ratings', 'tags_list', 'usd_price', 'product_imgs', 'details', 'price', 'product_file']

        def __init__(self, *args, **kwargs):
            super(ProductrListSerializer, self).__init__(*args, **kwargs)


class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)
    product_imgs = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title', 'image', 'publish_status', 'tags', 'slug',
                  'product_ratings', 'product_imgs', 'tags_list', 'details', 'usd_price', 'price', 'demo_url', 'product_file', 'downloads']

        def __init__(self, *args, **kwargs):
            super(ProductrListSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone']

        def __init__(self, *args, **kwargs):
            super(CustomerSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone', 'profile_img', 'customer_orders']

        def __init__(self, *args, **kwargs):
            super(CustomerDetailSerializer, self).__init__(*args, **kwargs)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer',  'order_status',
                  'total_amout', 'total_usd_amount', 'order_time']

        def __init__(self, *args, **kwargs):
            super(OrderSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1

        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['customer'] = CustomerSerializer(instance.customer).data
            return response


class OrderItemSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    # product = ProductDetailSerializer()

    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'qty', 'price', 'order', 'usd_price']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrderItemSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['order'] = OrderSerializer(instance.order).data
        response['customer'] = CustomerSerializer(instance.order.customer).data
        response['user'] = UserSerializer(instance.order.customer.user).data
        response['product'] = ProductDetailSerializer(instance.product).data

        return response


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
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
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer).data
        response['user'] = UserSerializer(instance.customer.user).data
        return response

    class Meta:
        model = ProductRating
        fields = ['id', 'customer', 'product', 'rating', 'reviews', 'add_time']

        def __init__(self, *args, **kwargs):
            super(ProductRatingSerializer, self).__init__(*args, **kwargs)


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


# Wishlist
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'product', 'customer']

    def __init__(self, *args, **kwargs):
        super(WishlistSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer).data
        response['product'] = ProductDetailSerializer(instance.product).data
        return response
