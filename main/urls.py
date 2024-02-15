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

    # order
    path('orders/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),


    # customer address
    # path('customer-address/', views.CustomerAddress.as_view()),
]

urlpatterns += router.urls
