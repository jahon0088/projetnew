from rest_framework import serializers
from register.models import User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class ProductSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"