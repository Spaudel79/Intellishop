from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination

# List and create products

class ProductPagination(PageNumberPagination):
    page_size = 8

class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ProductPagination

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse("Product List View is working")


    # def get_queryset(self):
    #     print("i am here")
    #     breakpoint()
    #     return super().get_queryset()

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  # Only authenticated users can create and view products

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)  # Set the user who created the product

# Retrieve, update, and delete products
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update or delete products

    def get_object(self):
        obj = super().get_object()
        if obj.created_by != self.request.user:
            raise PermissionDenied("You don't have permission to access this product")
        return obj


