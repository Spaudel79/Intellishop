from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from surprise import Dataset, Reader, SVD
import pandas as pd
from rest_framework.views import APIView
from .models import Rating, Product

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
    permission_classes = [AllowAny]  # Only authenticated users can update or delete products

    # def get_object(self):
    #     obj = super().get_object()
    #     if obj.created_by != self.request.user:
    #         raise PermissionDenied("You don't have permission to access this product")
    #     return obj

#  Recommendations login

class RecommendationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        
        # Get user_id from query params
        user_id = request.query_params.get('user_id')

        if not user_id:
            # Return all products if no user_id is provided
            products = Product.objects.all().values('id', 'item_name', 'new_price', 'description', 'image')
            return Response(list(products))

        # Fetch ratings from database
        ratings = Rating.objects.all().values('user_id', 'item_id', 'rating')
        df = pd.DataFrame(list(ratings))

        # Train recommendation model (basic example)
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
        algo = SVD()
        trainset = data.build_full_trainset()
        algo.fit(trainset)

        # Generate recommendations for the user
        item_ids = Product.objects.values_list('id', flat=True)
        recommendations = [
            {
                "item_id": item_id,
                "predicted_rating": algo.predict(user_id, item_id).est,
                "item_name": Product.objects.get(id=item_id).item_name,
                "new_price": Product.objects.get(id=item_id).new_price,
                "description": Product.objects.get(id=item_id).description,
                "image": Product.objects.get(id=item_id).image.url,
            }
            for item_id in item_ids
        ]

        # Sort recommendations by predicted rating
        recommendations = sorted(recommendations, key=lambda x: x['predicted_rating'], reverse=True)

        return Response(recommendations[:10])  # Return top 10 recommendations


