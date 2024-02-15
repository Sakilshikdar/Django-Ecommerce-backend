from django.shortcuts import render
from .import serializers
from rest_framework import generics, permissions, pagination, viewsets
from .models import Vendor, Product, ProductCatorgory, Customer, Order, OrderItem, CustomerAddress, ProductRating

# Create your views here.


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductrListSerializer
    pegination_classes = pagination.PageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            category = ProductCatorgory.objects.get(id=category)
            qs = qs.filter(category=category)
        return qs


class TagProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductrListSerializer
    pegination_classes = pagination.PageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['tag']
        if tag:
            qs = qs.filter(tags__icontains=tag)
        return qs


class RelatedProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductrListSerializer
    pegination_classes = pagination.PageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        product_id = self.kwargs['pk']
        product = Product.objects.get(id=product_id)
        category = product.category
        if category:
            qs = qs.filter(category=category).exclude(id=product_id)
        return qs


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.PeoductDetailSerializer

# customer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer


# order

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = OrderItem.objects.all()
    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(pk=order_id)
        order_items = OrderItem.objects.filter(order=order)
        return order_items


# customer address

class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = serializers.CustomerAddressSerializer


# ratting7
class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = serializers.ProductRatingSerializer


# category

class CatagoryList(generics.ListCreateAPIView):
    queryset = ProductCatorgory.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCatorgory.objects.all()
    serializer_class = serializers.CategoryeDtailSerializer
