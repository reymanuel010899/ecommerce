from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import electronicomodel
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db.models import Q
from .models import categoria
from .models import electronicomodel
from .forms import electronicoform
from django.db.models import  Sum
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import vistas, ofertas_descuentos
from django.contrib.auth import logout
from .models import categoria

#Create your views here


def  home(request):
    if request.user.is_authenticated:
        oferta_1 = ofertas_descuentos.objects.filtrar_ofertas_por_fecha()      
        laptops =  electronicomodel.objects.all().order_by('created')[:]
        vista = vistas.objects.filter(user=request.user).exclude(articulo__id__in=[34,37,27]).order_by('-created')[:4]
        categoria_oferta = electronicomodel.objects.filter(in_portada=True).order_by('created')[4:8]
        categorias = electronicomodel.objects.filter(in_portada=True).order_by('created')[:4]
        deportes = electronicomodel.objects.filter(categoria__id = '2')[:4]
        mas_vistos = vistas.objects.productos_mas_visitados()
        lista = electronicomodel.objects.filter(id__in=mas_vistos)
        ropa = electronicomodel.objects.filter(categoria__id='5').exclude(id__in=[24,29] )[:4]
        articulo = electronicomodel.objects.all().order_by('-created').exclude(id__in=[22,23.24,30,29,28])[:8]
        return render(request, 'index.html', {'laptops':laptops,'vistas':vista,'deportes':deportes, 'categorias':categorias,'categorias_oferta':categoria_oferta, 'portada1':oferta_1,'mas':lista, 'ropa':ropa,'articulo':articulo})
    else:
        ropa = electronicomodel.objects.filter(categoria__id='5').exclude(id__in=[24,29] )[:4]
        articulo = electronicomodel.objects.all().order_by('-created').exclude(id__in=[22,23.24,30,29,28])[:8]
        mas_vistos = vistas.objects.productos_mas_visitados()
        lista = electronicomodel.objects.filter(id__in=mas_vistos)
        categorias = electronicomodel.objects.filter(in_portada=True).order_by('-created')[:4]
        categoria_oferta = electronicomodel.objects.filter(in_portada=True).order_by('-created')[4:8]
        deportes = electronicomodel.objects.filter(categoria__id = '2')[:4]
        laptop =  electronicomodel.objects.all().order_by('created')[:]
        return render(request, 'index.html',{'laptops':laptop, 'deportes':deportes,'categorias':categorias,'categorias_oferta':categoria_oferta, 'mas':lista,'articulo':articulo, 'ropa':ropa})


 

def electrodomesticosview(request):
   
        laptop = electronicomodel.objects.filter(categoria__id='6' ).exclude(id__in=[22,30,23])
        paginator = Paginator(laptop, 8)
        num_page = request.GET.get('page')
        page = paginator.get_page(num_page)
        return render(request, 'electronico.html', {'page':page})    


def lectroctronicoview(request, pk):

        laptop = electronicomodel.objects.filter(categoria__id=pk ).exclude(id__in=[22,30,23,27,34])
        paginator = Paginator(laptop, 8)
        num_page = request.GET.get('page')
        page = paginator.get_page(num_page)
        return render(request, 'electronico.html', {'page':page})    
   


def iniciarsecionview(request):
        if request.method == 'GET':
            return render(request, 'iniciar_secion.html')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if not user:
                return  render(request, 'iniciar_secion.html', {'error':'esta cuenta no existe'})
            else:
                login(request,user)
                return redirect('inicio:inicio')
    
def registrar_user(request):
    if request.method == 'GET':
        return render(request, 'registraruser.html')
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'registraruser.html', {'error':'contraseñas invalidas'} )
        else:
            username = request.POST['username']
            try:
                user = User.objects.create_user(username=username, password=request.POST['password1'])
                login(request, user)
                return redirect('inicio:inicio')
            except:
                 return render(request, 'registraruser.html', {'error':'username already exist'} )


def busqueda_contenido(request):
    contenido = request.GET.get('contenido')
    url = request.GET.get('url')
    if url == 'electronicos':
        electrico = electronicomodel.objects.filter(Q(titulo__icontains= contenido) | Q(modelo__icontains = contenido))
        return render(request, 'busqueda.html', {"electronicos":electrico})
    elif url == 'hombres': 
        pass
    elif url == 'mujer':
        pass
    elif url == 'niños':
        pass
    elif url == 'electrodomesticos':
        pass
    elif url == 'deportes':
        pass
    else:
        electrico = electronicomodel.objects.filter(Q(titulo__icontains= contenido) | Q(modelo__icontains = contenido) )
        return render(request, 'busqueda.html', {"electronicos":electrico})


# class detalle_producto(DetailView):
#     template_name = 'detalle-producto.html'
#     model = electronicomodel
    
    
#     def get_context_data(self, **kwargs):
#         pk = self.kwargs['pk']
#         descuento = self.request.GET.get('total','')
#         context = super().get_context_data(**kwargs)
#         if descuento != '':
#             descuento = float(descuento)
#             producto = electronicomodel.objects.get(id=pk)
#             producto.precio = descuento
#             context["producto"] = producto
#             id_categoria = categoria.objects.obtener_categoria(pk)
#             id_categoria = id_categoria.id
#             context["lista"] = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id__in= [24,29]).order_by('-created')[:8]
#             context["forma"] = electronicoform
#             context["cantidad"] =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('cantidad') )
#             return context
#         else:
#             context["producto"] = electronicomodel.objects.get(id=pk)
#             id_categoria = categoria.objects.obtener_categoria(pk)
#             id_categoria = id_categoria.id
#             context["lista"] = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id__in= [24,29]).order_by('-created')[:8]
#             context["forma"] = electronicoform
#             context["cantidad"] =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('cantidad') )
#             return context

#     def get_object(self, **kwargs):
#         object =  super().get_object(**kwargs)
#         if self.request.user.is_authenticated:
#             vistas.objects.get_or_create(user=self.request.user, articulo = object )   
#         return object
    
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'pk':self.kwargs['pk']})
#         return kwargs
   
def detalle_producto(request, pk):
    if request.method == 'GET':
        if request.user.is_authenticated:
            descuento = request.GET.get('total','')
            if descuento != '':
                descuento = float(descuento)
                producto = electronicomodel.objects.get(id=pk)
                producto.precio = descuento
                producto.save()
                id_categoria = categoria.objects.obtener_categoria(pk)
                id_categoria = id_categoria.id
                lista = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id__in= [24,29]).order_by('-created')[:8]
                cantidad =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('cantidad') )
                vistas.objects.get_or_create(user=request.user, articulo=producto)
                return render(request, 'detalle-producto.html', {'producto':producto, 'lista':lista, 'forma':electronicoform,'cantidad':cantidad})
            else:
                producto = electronicomodel.objects.get(id=pk)
                id_categoria = categoria.objects.obtener_categoria(pk)
                lista = electronicomodel.objects.filter(categoria__id = id_categoria.id).exclude(id__in= [24,29]).order_by('-created')[:8]
                cantidad =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('cantidad') )
                vistas.objects.get_or_create(user=request.user, articulo=producto)
                return render(request, 'detalle-producto.html', {'producto':producto, 'lista':lista, 'forma':electronicoform,'cantidad':cantidad})
        else:
            return redirect('inicio:registrate')
    
        


def detalle_favorito(request, pk):
    descuento = request.GET.get('total','')
    print(descuento)
    producto = electronicomodel.objects.get(id=pk)
    producto.precio = descuento
    producto.save()
    producto_id = producto.id
    id_categoria = categoria.objects.obtener_categoria(producto_id)
    id_categoria = id_categoria.id
    lista = electronicomodel.objects.filter(categoria__id = id_categoria).exclude(id=pk)[:8]
 
    cantidad =  electronicomodel.objects.filter(id=pk).aggregate(cantida_stok = Sum('cantidad') )
    return render(request, 'detalle-favorito.html', {'productos':producto, 'cantidad':cantidad, 'forma':electronicoform, 'lista':lista})

def salir_seccion(request):
    logout(request)
    return redirect('inicio:identificate')



#listando los articulos que estan en ofertas de la categoria deportes

def listar_prod_ofertas_categoria(request, pk):
    ofertas = ofertas_descuentos.objects.listar_ofertas(pk)
    return render(request, 'oferta_deportes.html', {'page':ofertas})



def listar_prod_ofertas_moda_categoria(request, pk):
    ofertas = ofertas_descuentos.objects.listar_ofertas(pk)
    return render(request, 'moda_ofertas.html', {'page':ofertas})


def convertir_product(reuqest, pk):
   pro = electronicomodel.objects.get(oferta_devolver__id=pk) 
   id_producto = pro.id
   return redirect('inicio:detalle-productos', pk=id_producto)


def listar_celulares(request):
    lista = electronicomodel.objects.filter(categoria__id='7')
    paginator = Paginator(lista, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page)  
    return render(request,'listar_cell.html', {'page':page})

def listar_acesorio(request):
    lista = electronicomodel.objects.filter(categoria__id='3').exclude(id__in=[27,34])
    paginator = Paginator(lista, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'listar_acesorio.html', {'page':page})


def listar_pc(request):
    lista = electronicomodel.objects.filter(categoria__id='14')
    paginator = Paginator(lista, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request,'listar_pc.html',{'page':page})

