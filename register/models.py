from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, is_active=True, is_staff=False, is_superuser=False, *args, **kwargs):
        user = self.model(
            phone=phone,
            password=password,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, phone, password, *args, **kwargs):
        return self.create_user(phone, password, is_staff=True, is_superuser=True, *args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(editable=False, auto_now_add=True)

    USERNAME_FIELD = 'phone'
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['name']

    def res(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
        }

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    view = models.IntegerField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

