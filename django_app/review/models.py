from django.conf import settings
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey('product.Product')
    score = models.IntegerField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)