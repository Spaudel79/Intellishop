from django.urls import path
from . import views
from .views import *

urlpatterns = [


    # Product API endpoints
    path('api/products', views.ProductView.as_view(), name='products-list'),
    # path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
]
