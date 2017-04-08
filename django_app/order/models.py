from django.conf import settings
from django.db import models


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey('product.Product')
    count = models.IntegerField()

    def __str__(self):
        return 'Cart | User[{}], Product[{}], Count[{:,}]'.format(
            self.user,
            self.product.title,
            self.count
        )


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    # 배송정보
    name = models.CharField(max_length=64)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    postcode = models.CharField(max_length=6)
    delivery_fee = models.IntegerField()

    # 주문정보
    point = models.IntegerField()
    amount = models.IntegerField()
    state = models.IntegerField()

    # 아임포트 transaction id
    tid = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order | User[{}], Amount[{:,}]'.format(
            self.user,
            self.amount
        )


class OrderProductItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey('product.Product')
    count = models.IntegerField()
    point = models.IntegerField()
    discount = models.IntegerField()
    amount = models.IntegerField()
