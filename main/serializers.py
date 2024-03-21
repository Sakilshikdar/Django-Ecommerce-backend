from rest_framework import serializers
from .models import Vendor, ProductCatorgory, Product, Customer, Order, OrderItems, CustomerAddress, ProductRating, ProductImage, Wishlist


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

    product_imgs = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title',
                  'product_ratings', 'tags_list', 'usd_price', 'product_imgs', 'details', 'price', 'product_file']

        def __init__(self, *args, **kwargs):
            super(ProductrListSerializer, self).__init__(*args, **kwargs)


class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)
    product_imgs = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'vendor', 'title',
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


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone']

        def __init__(self, *args, **kwargs):
            super(CustomerDetailSerializer, self).__init__(*args, **kwargs)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_status']

        def __init__(self, *args, **kwargs):
            super(OrderSerializer, self).__init__(*args, **kwargs)


class OrderItemSerializer(serializers.ModelSerializer):
    # order = OrderSerializer()
    # product = ProductDetailSerializer()

    class Meta:
        model = OrderItems
        fields = ['id', 'product', 'qty', 'price', 'order']
        # fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['order'] = OrderSerializer(instance.order).data
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
