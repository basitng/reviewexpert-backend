from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ListOfProducts.as_view(), name='Home'),
    path('product/create/', CreateProduct.as_view(), name='Home'),
    path('product/<str:id>/', getOneProduct.as_view(), name='Single product'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='Delete product'),
    path('update/<int:pk>/', UpdateProduct.as_view(), name='Update post'),
    
    path('reviews/', ReviewProductList.as_view(), name='All Reviewed Product'),
    path('review/product/', ReviewProductView.as_view(), name='Review Product'),
    
    path('brand/profiles/', BrandProfile.as_view(), name='List of all profiles'),
    path('brand/profile/update/<int:pk>/', BrandProfileUpdate.as_view(), name='Update One Profile'),
    
    path('reviewer/profiles/', ReviewerProfile.as_view(), name='List of all profiles'),
    path('reviewer/profile/update/<int:pk>/', ReviewerProfileUpdate.as_view(), name='Update One Profile'),
    
    path('register/reviewer/', RegisterReviewer.as_view(), name='register reviewer'),
    path('register/brand/', RegisterBrand.as_view(), name='register reviewer'),

]
