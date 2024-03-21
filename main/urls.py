from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewSet)
router.register('productrating', views.ProductRatingViewSet)

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<int:pk>/', views.VendorDetail.as_view()),

    # product
    path('products/', views.ProductList.as_view()),
    path('products/<str:tag>', views.TagProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('related-products/<int:pk>/', views.RelatedProductList.as_view()),


    # category
    path('catagories/', views.CatagoryList.as_view()),
    path('catagory/<int:pk>/', views.CategoryDetail.as_view()),


    # cusotmer
    path('customers/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('customer/login/', views.customer_login, name='customer_login'),
    path('customer/register/', views.customer_register, name='customer_register'),

    # order
    path('orders/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    path('orderitems/', views.OrderItemList.as_view()),
    path('customer/<int:pk>/orderitems/',
         views.CustomerOrderItemList.as_view()),
    path('updateStatus/<int:order_id>/',
         views.updateStatus, name='update_orders_status'),
    path('update_product_download_count/<int:product_id>/',
         views.update_product_download_count, name='update_product_download_count'),

    # Wishlist
    path('wishlist/', views.Wishlistitem.as_view()),
    path('check_in_wishlist/',
         views.check_in_wishlist_items, name='check_in_wishlist'),
    path('remove_from_wishlist/',
         views.remove_from_wishlist_items, name='remove_from_wishlist'),

    path('customer/<int:pk>/wishitems/',
         views.CustomerWishItemList.as_view()),
]

urlpatterns += router.urls
