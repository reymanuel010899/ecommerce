from rest_framework import serializers, pagination
from inicio.models import electronicomodel, categoria
from carro_compra.models import carro_compras
class categoriaserial(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('nombre',)


class serialisarmodelo(serializers.HyperlinkedModelSerializer):
    categoria = categoriaserial()
    class Meta:
        model = electronicomodel
        fields = (  'id',
                    'titulo',
                    'modelo',
                    'marca',
                    'procesador',
                    'precio',
                    'avatar',
                    'almacenamiento',
                    'categoria'
                )
        extra_field = {
            'categoria': {

                'view_name':'inicio:detalle-productos', 'lookup_field':'pk'
            }

        }


class paginacion(pagination.PageNumberPagination):
    page_size = 2
    max_page_size = 10

class categoriarserializar(serializers.ModelSerializer):
   
    class Meta:
        model = categoria
        fields = ('nombre',)  

        


class crearserializar(serializers.ModelSerializer):
    categoria = categoriarserializar()
    class Meta:
        model = electronicomodel
        fields = (

            'titulo',
            'almacenamiento',
            'avatar',
            'rating',
            'categoria'
        )  

class actualizar(serializers.ModelSerializer):
    class Meta:
        model = electronicomodel
        fields = ('titulo',
        'modelo','marca',
        'categoria','rating','avatar')        
  

  
class categoriaserializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('marca',)
    


class productoss(serializers.ModelSerializer):
    class Meta:
        model = electronicomodel
        fields = ('__all__')


class user_sserialiser(serializers.Serializer):
    user = serializers.CharField()




class caroo_serializer(serializers.ModelSerializer):
    productos = productoss()
    class Meta:
        model = carro_compras
        fields = ('user','productos','cantidad')