from django.contrib import admin
from .models.producto import Producto
from .models.venta import Venta
from .models.factura import Factura
from .models.admin import Admin

admin.site.register(Admin)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Factura)