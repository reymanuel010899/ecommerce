from django.urls import path
from . import views
app_name = 'moda'

urlpatterns = [
    path('categoria-moda/<nombre>/', views.todo_sobre_moda, name='categoria-moda'),
    path('moda-principal', views.moda_views, name='modas'),
    path('oferta-by-categoy/<pk>/', views.definir_categoria, name='oferta-by-categoy'),
    path('listar-pantalones/', views.listar_pantalones, name='listar-pantalones'),
    path('listar-polochert/', views.listar_polochert, name='listar-polochert'),
    path('listar-tenis/', views.listar_tenis, name='listar-tenis'),
    path('listar-ropa-interior/', views.lista_ropa_interior, name='listar-ropa-interior'),
    path('listar-ropa-hombre/', views.listar_ropa_hombre, name='listar-ropa-hombre'),
    path('listar-ropa-mujer/', views.listar_ropa_mujer, name='listar-ropa-mujer'),
    path('listar-ropa-niño/', views.listar_ropa_niños, name='listar-ropa-niño'),
    path('listar-electrodomesticos/', views.listar_electrodomesticos, name='listar-electrodomesticos'),
    path('listar-deportes/', views.listar_articulo_deportes, name='listar-deportes'),
    path('listar-historial/',  views.listar_historial, name='listar-historial')
]
