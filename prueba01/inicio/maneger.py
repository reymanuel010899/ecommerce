from django.db import models
from rest_framework.generics import GenericAPIView
from django.db.models import Count, Sum, F


class electronicomanayer(models.Manager):
    def inicial(self):
        return []
    
    def obtener_filtros(self, tipo):
        if tipo == 'polochert':
            return self.filter(tipo_ropa = '1')
        elif tipo == 'pantalon':
            return self.filter(tipo_ropa = '2')
        elif tipo == 'tenis':
            return self.filter(tipo_ropa = '3')
        elif tipo == 'acesorios':
            return self.filter(tipo_ropa = '4')
        elif tipo == 'vestidos':
            return self.filter(tipo_ropa_mujer = '1')
        else:
            return self.filter(tipo_ropa = '1')

class categora_manayer(models.Manager):
    def obtener_categoria(self , producto_id):
        return self.get(categorias__id = producto_id)
    '''rest_framework'''


class electico_maneyer(models.Manager):
    def get_vistas_count(self):
        return self.vistas_set.all().count()       


class ofertas_manayer(models.Manager):
    def filtrar_ofertas_por_fecha(self):
        product = self.filter(in_port=True)
        return product

    def listar_ofertas(self, pk):
        productos = self.filter(producto__categoria__id=pk).annotate( descuent = Sum(F('producto__precio')-F('descuentos')*F('producto__precio')))
        return productos

    def listar_ofertas2(self, pk):
        productos = self.filter(producto__categoria__id=pk).order_by('producto__precio')
        precios = productos.precios
        return precios
    
class VistaManayer(models.Manager):


    def productos_mas_visitados(self):
        resultado = self.values('articulo__id').annotate(cantidad = Count('articulo')).order_by('-cantidad')[:4]
        lista = []
        for valor in resultado:
            lista.append(valor['articulo__id'])
        return lista





