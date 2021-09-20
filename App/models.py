from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from autoslug import AutoSlugField

class User(AbstractUser):
    is_reviewer = models.BooleanField(default=False)
    is_brand = models.BooleanField(default=False)

#Different Users Account

class Reviewer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.CharField(null=True, max_length=100)
    reviews = models.CharField(null=True, max_length=500)
    location = models.CharField(null=True, max_length=500)
    image = models.ImageField(blank=True, null=True, upload_to='reviewers_profile_pics/')

    def __str__(self):
        return self.user.username


class Brand(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    brand_name = models.CharField(null=True, max_length=100)
    brand_logo = models.ImageField(blank=True, null=True, upload_to='brand_profile_pics/')
    stars = models.CharField(null=True, max_length=100)
    reviews = models.CharField(null=True, max_length=500)
    location = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.user.username

class Tag(models.Model):
    tags = models.CharField(max_length=100, unique=True)

class Product(models.Model):
    product_publisher = models.ForeignKey(Brand, unique=False, on_delete=models.CASCADE)
    product_image = models.ImageField(blank=True, null=True, upload_to='images/')
    product_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    product_rating = models.CharField(max_length=500,null=True)
    product_stars = models.CharField(max_length=500,null=True)
    product_reviews = models.CharField(max_length=500,null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    slug = AutoSlugField(populate_from='timestamp', null=True, blank=True)
    def __str__(self):
        return self.product_name

class ReviewProduct(models.Model):
    reviewer = models.OneToOneField(Reviewer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    slug = AutoSlugField(populate_from='timestamp')
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    review = models.TextField()
    rating = models.CharField(max_length=100)
    def __str__(self):
        return self.product.product_name
