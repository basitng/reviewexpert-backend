from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

# LOCAL IMPORTS
from .models import Reviewer, Brand, Product, ReviewProduct

class ReviewerRegisterationSerializer(RegisterSerializer):
    reviewer = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_cleaned_data(self):
        data = super(ReviewerRegisterationSerializer,
            self).get_cleaned_data()
        return data

    def save(self, request):
        user = super(ReviewerRegisterationSerializer, self).save(request)
        user.is_reviewer = True
        user.save()

        reviewer = Reviewer(user=user)
        reviewer.save()
        return user
        print('Account created')
            
class BrandRegisterationSerializer(RegisterSerializer):
    brand = serializers.PrimaryKeyRelatedField(read_only=True)

    def get_cleaned_data(self):
        data = super(BrandRegisterationSerializer,
            self).get_cleaned_data()
        return data

    def save(self, request):
        user = super(BrandRegisterationSerializer, self).save(request)
        user.is_brand = True
        user.save()

        brand = Brand(user=user)
        brand.save()
        return user
        print('Account created')
            

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_publisher', 'product_rating',
         'product_stars', 'product_image','slug',
          'product_name', 'product_reviews', 'description')
        

class RevieweProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewProduct
        fields = ['reviewer', 'product', 'review', 'slug', 'rating']

class BrandProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('brand_name', 'brand_logo', 'stars', 'reviews', 'location')

class ReviewerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ('user', 'image',  'stars', 'reviews', 'location')

