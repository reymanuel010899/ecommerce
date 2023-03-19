from django.shortcuts import render, redirect
from .models import carro_compras
from inicio.models import electronicomodel
from inicio.models import vistas


# Create your views here.
def agregar_producto_carro(request, pk):
  
      producto = electronicomodel.objects.get(id=pk)
      if request.user.is_authenticated:
            if request.method == 'GET':
                  ap , cr = carro_compras.objects.get_or_create(
                              productos = producto,
                              defaults={
                                    'user':request.user,
                                    'cantidad':1
                              }
                        
                              )
      
                  return render(request, 'confirmacion.html', {'producto':ap.productos.modelo} )
            else:
                  cantidades = request.POST.get('cantidad')
                 
                  if int(cantidades) > producto.cantidad:

                        ap , cr = carro_compras.objects.get_or_create(
                              productos = producto,
                              defaults={
                              'user': request.user,
                              'cantidad':producto.cantidad
                              }
                              )
                  else:

                              ap , cr = carro_compras.objects.get_or_create(
                              productos = producto,
                              defaults={
                                    'user':request.user,
                                    'cantidad':cantidades
                              }
                              )
                         
                  return render(request, 'confirmacion.html', {'producto':ap.productos.titulo, 'imagen':ap} )

      else:
            return redirect('inicio:registrate')    


def carro_compra(request):
      if request.user.is_authenticated:
            if request.method == 'GET':
                  ultimas = vistas.objects.filter(user=request.user).exclude(articulo__id__in=[30,29,34,28,27,23,22,24]).order_by('-created')
                  producto = carro_compras.objects.filter(user=request.user).order_by('-created')

                  return render(request, 'carro-compras.html', {'productos':producto,"ultimas":ultimas})  
      else:
            return render(request, 'carro-compras.html') 
      

def gregar_ultimos_productos_vistos(request, pk):
      product = electronicomodel.objects.get(devolver_views__id=pk)
      return redirect('carro_compra:agregar-producto', pk=product.id)


def eliminar_productos(request, pk):
      prod = carro_compras.objects.get(productos__id=pk)
      prod.delete()
      return redirect('carro_compra:carro-compra')



# en esta vista aumento la cantidad del producto y cuando llega al valor maximo que tiene el producto le devuelvo un mensaje
def aumentando_cantidad(request, pk):
      producto = carro_compras.objects.get(id=pk)
      if  (producto.cantidad) < int(producto.productos.cantidad):
            producto.cantidad = producto.cantidad  + 1  
            producto.save()
            return redirect('carro_compra:carro-compra')
      else:  
            producto.cantidad = producto.cantidad 
            producto.save()
            return redirect('carro_compra:carro-compra')
    




# en esta vista disminullo la cantidad del producto y cuando llega a 0 la elimina
def disminuir_cantidad(request, pk):
      producto = carro_compras.objects.get(id=pk)
      producto.cantidad =  producto.cantidad - 1
      if producto.cantidad == 0:
            return redirect('carro_compra:carro-compra')
      producto.save()
      return redirect('carro_compra:carro-compra')


def convertir_vistas_by_productos(request, pk):
      producto = electronicomodel.objects.get(devolver_views__id=pk)
      return redirect('inicio:detalle-faborito', pk=producto.id)


