from django.contrib import admin

# Register your models here.
from register.models import Product, User

admin.site.register(User)
admin.site.register(Product)