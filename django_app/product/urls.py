from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', views.ProductDetail.as_view(), name='detail'),
]
