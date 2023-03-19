from django.urls import path
from . import views
#electrodomesticosview, 
# registrar_user,busqueda_contenido, detalle_producto,
#  detalle_favorito , iniciarsecionview, salir_seccion,
#  listar_prod_ofertas_categoria,
#  listar_prod_ofertas_moda_categoria,
#  convertir_product,listar_celulares,listar_acesorio,listar_pc)

 
app_name = 'inicio'

urlpatterns = [
    path('', views.home, name='inicio'),
    path("electrodomesticos/", views.electrodomesticosview, name='electrodomesticos'),
    path('identificate/', views.iniciarsecionview, name='identificate'),
    path('registrate/', views.registrar_user, name='registrate'),
    path('busqueda-contenido/',views.busqueda_contenido , name='busqueda-contenido'),
    path('detalle-productos/<pk>/', views.detalle_producto, name='detalle-productos'),
    path('detalle-faborito/<pk>/', views.detalle_favorito, name='detalle-faborito'),
    path('salir-seccion/', views.salir_seccion, name='salir-seccion'),
    path('listar-oferta-categoria/<pk>/', views.listar_prod_ofertas_categoria, name='listar-oferta-categoria'),
    path('oferta-moda-categoria/<pk>/', views.listar_prod_ofertas_moda_categoria, name='listar-moda-categoria'),
    path('convertir-a-productos/<pk>/',views.convertir_product, name='convertir'),
    path('listar-celulares/', views.listar_celulares, name='listar-movie'),
    path('listar-acesorio/', views.listar_acesorio, name='listar-acesorio'),
    path('listar-pc/', views.listar_pc, name='listar-pc'),
    path('listar-electronico/<pk>/', views.lectroctronicoview, name='listar-electronicos'),
    
    ]
