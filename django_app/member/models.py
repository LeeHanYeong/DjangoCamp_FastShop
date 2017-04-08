from django.contrib.auth.models import AbstractUser, UserManager as AuthUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(AuthUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user_level, _ = UserLevel.objects.get_or_create(
            title='Basic',
            min_point=0,
            point_rate=0
        )
        extra_fields.setdefault('level', user_level)
        return super()._create_user(username, email, password, **extra_fields)


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

    objects = UserManager()

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
    content = models.TextField()
    delta = models.IntegerField()
