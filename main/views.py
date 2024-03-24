from django.shortcuts import render
from .import serializers
from rest_framework import generics, permissions, pagination, viewsets
from .models import Vendor, Product, ProductCatorgory, Customer, Order, OrderItems, CustomerAddress, ProductRating, Wishlist, ProductImage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.


@csrf_exempt
def customer_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')

    try:
        # Create a new user
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        if user:
            try:
                customer = Customer.objects.create(user=user, phone=mobile)
                msg = {
                    'bool': True,
                    'user': user.id,
                    'customer': customer.id,
                    'msg': 'You have successfully registered.You can now login.'
                }
            except IntegrityError:
                msg = {
                    'bool': False,
                    'msg': 'mobile already exists'
                }
        else:
            msg = {
                'bool': False,
                'msg': 'Oops! Something went wrong. Please try again later.'
            }
    except IntegrityError:
        msg = {
            'bool': False,
            'msg': 'username already exist'
        }
    return JsonResponse(msg)


@csrf_exempt
def customer_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        customer = Customer.objects.get(user=user)
        msg = {
            'bool': True,
            'user': user.username,
            'id': customer.id,
        }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid username or password'
        }

    return JsonResponse(msg)


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer


@csrf_exempt
def vendor_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    address = request.POST.get('address')

    try:
        # Create a new user
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        if user:
            try:
                vendor = Vendor.objects.create(
                    user=user, phone=phone, address=address)
                msg = {
                    'bool': True,
                    'user': user.id,
                    'customer': vendor.id,
                    'msg': 'You have successfully registered.You can now login.'
                }
            except IntegrityError:
                msg = {
                    'bool': False,
                    'msg': 'mobile already exists'
                }
        else:
            msg = {
                'bool': False,
                'msg': 'Oops! Something went wrong. Please try again later.'
            }
    except IntegrityError:
        msg = {
            'bool': False,
            'msg': 'username already exist'
        }
    return JsonResponse(msg)


@csrf_exempt
def vendor_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        vendor = Vendor.objects.get(user=user)
        msg = {
            'bool': True,
            'user': user.username,
            'id': vendor.id,
        }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid username or password'
        }

    return JsonResponse(msg)


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
        if 'fetch_limit' in self.request.GET:
            limit = int(self.request.GET['fetch_limit'])
            qs = qs[:limit]
        return qs


class ProducImgstList(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer


class ProducImgstDetail(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        product_id = self.kwargs['product_id']
        if tag:
            qs = qs.filter(product_id=product_id)
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
        # print(product.image)
        category = product.category
        if category:
            qs = qs.filter(category=category).exclude(id=product_id)
        return qs


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer

# customer


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CustomerDetailSerializer

# order


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderItemList(generics.ListAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer_id = self.kwargs['pk']
        qs = qs.filter(order__customer__id=customer_id)
        return qs


class CustomerOrderItemList(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer_id = self.kwargs['pk']
        qs = qs.filter(order__customer__id=customer_id)
        return qs


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

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


@csrf_exempt
def updateStatus(request, order_id):
    msg = {
        'bool': False,
    }
    if request.method == "POST":
        updateRes = Order.objects.filter(
            id=order_id).update(order_status=True)
        # print(updateRes)
        if updateRes:
            msg = {
                'bool': True,
            }
    return JsonResponse(msg)


@csrf_exempt
def update_product_download_count(request, product_id):
    msg = {
        'bool': False,
    }
    if request.method == "POST":
        product = Product.objects.get(id=product_id)
        totalDownloads = int(product.downloads)

        totalDownloads += 1
        if totalDownloads == 0:
            totalDownloads = 1
        updateRes = Product.objects.filter(id=product_id).update(
            downloads=totalDownloads)
        if updateRes:
            msg = {
                'bool': True,
            }
    return JsonResponse(msg)

# wishlish


class Wishlistitem(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer


@csrf_exempt
def check_in_wishlist_items(request):
    msg = {
        'bool': False,
    }
    if request.method == "POST":
        product_id = request.POST.get('product')
        customer_id = request.POST.get('customer')
        checkWishlist = Wishlist.objects.filter(
            product__id=product_id, customer__id=customer_id).count()
        if checkWishlist > 0:
            msg = {
                'bool': True
            }
    return JsonResponse(msg)


class CustomerWishItemList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer_id = self.kwargs['pk']
        qs = qs.filter(customer__id=customer_id)
        return qs


@csrf_exempt
def remove_from_wishlist_items(request):
    if request.method == "POST":
        wishlist_id = request.POST.get('wishlist_id')
        res = Wishlist.objects.filter(id=wishlist_id).delete()
        msg = {
            'bool': False,
        }
        if res:
            msg = {
                'bool': True
            }
    return JsonResponse(msg)


class CustomerAddressItemList(generics.ListCreateAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = serializers.CustomerAddressSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer_id = self.kwargs['pk']
        qs = qs.filter(customer__id=customer_id).order_by('-default_address')
        return qs


@csrf_exempt
def mark_default_address(request, pk):
    if request.method == "POST":
        address_id = request.POST.get('address_id')
        res = CustomerAddress.objects.all().update(default_address=False)
        res = CustomerAddress.objects.filter(
            id=address_id).update(default_address=True)
        msg = {
            'bool': False,
        }
        if res:
            msg = {
                'bool': True
            }
    return JsonResponse(msg)


def customer_dashboard(request, pk):
    customer_id = pk
    totalWishList = Wishlist.objects.filter(
        customer__id=customer_id).count()
    totalAddress = CustomerAddress.objects.filter(
        customer__id=customer_id).count()
    totalOrders = Order.objects.filter(
        customer__id=customer_id).count()
    msg = {
        'totalOrders': totalOrders,
        'totalAddress': totalAddress,
        'totalWishList': totalWishList,
    }
    return JsonResponse(msg)
