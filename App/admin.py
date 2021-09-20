from django.contrib import admin

from .models import Reviewer, Brand, User,Product, ReviewProduct

admin.site.register(Reviewer)
admin.site.register(Brand)
admin.site.register(User)
admin.site.register(ReviewProduct)
admin.site.register(Product)
