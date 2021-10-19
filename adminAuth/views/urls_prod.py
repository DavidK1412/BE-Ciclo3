from django.conf.urls import url
from django.urls.conf import path
from .productoCreateview import producto_api, producto_detail

urlpatterns = [
    path('', producto_api),
    path('<int:pk>', producto_detail)
]
