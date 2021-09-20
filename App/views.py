from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_auth.registration.views import RegisterView

from .models import (
    Product, 
    Brand,
    Reviewer,
    ReviewProduct,
)
from .serializers import ProductSerializer

from .serializers import (
    ReviewerRegisterationSerializer,
    BrandRegisterationSerializer,
    BrandProfileSerializer,
    RevieweProductSerializer,
    ReviewerProfileSerializer
)

#
class ListOfProducts(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class getOneProduct(APIView):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

#Just for brands
class CreateProduct(APIView):
    parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        print(f'> ========== {request.data} ============')
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewProductView(generics.CreateAPIView):
    serializer_class = RevieweProductSerializer
    queryset = ReviewProduct.objects.all()

class ReviewProductList(generics.ListAPIView):
    serializer_class = RevieweProductSerializer
    queryset = ReviewProduct.objects.all()

class BrandProfile(generics.ListAPIView):
    serializer_class = BrandProfileSerializer
    queryset = Brand.objects.all()

class BrandProfileUpdate(generics.UpdateAPIView):
    serializer_class = BrandProfileSerializer
    queryset = Brand.objects.all()

class ReviewerProfile(generics.ListAPIView):
    serializer_class = ReviewerProfileSerializer
    queryset = Reviewer.objects.all()

class ReviewerProfileUpdate(generics.UpdateAPIView):
    serializer_class = ReviewerProfileSerializer
    queryset = Reviewer.objects.all()

class UpdateProduct(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
        
class DeleteProduct(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
        

class RegisterReviewer(RegisterView):
    serializer_class = ReviewerRegisterationSerializer

class RegisterBrand(RegisterView):
    serializer_class = BrandRegisterationSerializer

