from django.urls import path
from . import views
#from .views import agregar_producto_carro, eliminar_productos, carro_compra, gregar_ultimos_productos_vistos,aumentando_cantidad,disminuir_cantidad, convertir_vistas_by_productos

app_name = 'carro_compra'

urlpatterns = [
    path('agregar-producto/<pk>/',views. agregar_producto_carro, name='agregar-producto'),
    path('carro-compra/',views. carro_compra, name='carro-compra' ),
    path('eliminar-producto/<pk>/',views. eliminar_productos, name='eliminar-producto'),
    path('ultimos-productos/<pk>/',views. gregar_ultimos_productos_vistos, name='ultimos'),
    path('agregarndo/<pk>/', views.aumentando_cantidad, name='agregar-uno-mas'),
    path('disminuir/<pk>/', views.disminuir_cantidad, name='disminuir-uno-mas'),
    path('convertir-ultima-vista/<pk>/', views.convertir_vistas_by_productos, name='convertir-ultima-vista')
]
