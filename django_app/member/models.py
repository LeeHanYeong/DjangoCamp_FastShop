from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    CHOICES_GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    birthday = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICES_GENDER, blank=True)
    postcode = models.CharField(max_length=6, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    point = models.IntegerField(default=0)
    level = models.ForeignKey('UserLevel')
    wishlist = models.ManyToManyField('product.Product')

    def __str__(self):
        return self.username


class UserLevel(models.Model):
    title = models.CharField(max_length=64)
    min_point = models.IntegerField()
    point_rate = models.FloatField()

    def __str__(self):
        return self.title


class PointHistory(models.Model):
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    delta = models.IntegerField()
