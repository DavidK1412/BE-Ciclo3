from django.conf.urls import url
from django.urls.conf import path
from .ventaView import venta_api, venta_detail

urlpatterns = [
    path('', venta_api),
    path('<int:pk>', venta_detail)
]