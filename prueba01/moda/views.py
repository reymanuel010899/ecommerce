from django.shortcuts import render, HttpResponse, redirect
from inicio.models import categoria
from inicio.models import electronicomodel
from django.core.paginator import Paginator
from inicio.models import categoria
from inicio.models import vistas
# Create your views here.

def todo_sobre_moda(request, nombre):
    categori = categoria.objects.get(nombre=nombre)
    if nombre == 'deporte':
        return HttpResponse('deportes')
    elif nombre == 'electronic':
        return redirect('inicio:listar-electronicos', pk=categori.pk)
    elif nombre == 'moda':
        return redirect('moda:modas')
    elif nombre == 'electrodomesticos':
        return redirect('inicio:electrodomesticos')
    elif nombre == 'acesorios':
        return redirect('inicio:listar-electronicos', pk=categori.pk)
    else:
        return render(request, 'deporte.html')




#h aqui resivimos  la categoria y retornamos a una vista para hacer los filtros devidos por ofertas
def definir_categoria(request, pk):
    categorias = categoria.objects.get(categorias__id = pk)
    categoria_nombre = categorias.nombre

    if categoria_nombre == 'electrodomesticos':
        return redirect('inicio:listar-oferta-categoria', pk=categorias.id)
    elif categoria_nombre == 'moda':
        return redirect('inicio:listar-oferta-categoria', pk=categorias.id)
    elif categoria_nombre == 'acesorios':
       return redirect('inicio:listar-oferta-categoria', pk=categorias.id)
    elif categoria_nombre == 'deporte':
        return redirect('inicio:listar-oferta-categoria', pk=categorias.id)
    elif categoria_nombre == 'electronic':
        return redirect('inicio:listar-oferta-categoria', pk=categorias.id)
    else:
        return HttpResponse('electronico')            
    
    
def listar_pantalones(request):
    pantalones = electronicomodel.objects.filter(tipo_ropa = '2')
    paginator = Paginator(pantalones, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html', {'page':page})

def listar_polochert(request):
    pantalones = electronicomodel.objects.filter(tipo_ropa = '1')
    paginator = Paginator(pantalones, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request,'electrodomesticos.html',{'page':page})


def listar_tenis(request):
    tenis = electronicomodel.objects.filter(tipo_ropa='3')
    paginator = Paginator(tenis, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request,'electrodomesticos.html', {'page':page})

def  lista_ropa_interior(request):
    tenis = electronicomodel.objects.filter(tipo_ropa='4')
    paginator = Paginator(tenis, 20)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})

def listar_ropa_hombre(request):
    ropa_hombre = electronicomodel.objects.filter(categoria__id='5').exclude(id__in=[29,24,41])
    paginator = Paginator(ropa_hombre, 40)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})

def listar_ropa_mujer(request):
    tenis = electronicomodel.objects.filter(tipa_genero='2').exclude(id__in=[29,24,41])
    paginator = Paginator(tenis, 40)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})


def listar_ropa_niños(request):
    ropa_niño = electronicomodel.objects.filter(tipa_genero='3').exclude(id__in=[29,24,41])
    paginator = Paginator(ropa_niño, 40)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})



def listar_electrodomesticos(request):
    electro = electronicomodel.objects.filter(categoria__id='6').order_by("-created")
    paginator = Paginator(electro, 40)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})

def listar_articulo_deportes(request):
    articulo = electronicomodel.objects.filter(categoria__id='2').exclude(id__in=[28]) .order_by("-created")
    paginator = Paginator(articulo, 40)
    num_page = request.GET.get('page')
    page = paginator.get_page(num_page) 
    return render(request, 'electrodomesticos.html',{'page':page})



def listar_historial(request):
    if request.user.is_authenticated:
        ultimas_vistas = vistas.objects.filter(user=request.user).order_by('-created')
        paginator = Paginator(ultimas_vistas, 40)
        num_page = request.GET.get('page')
        page = paginator.get_page(num_page) 
        return render(request, 'listar_historial.html',{'page':page})
    else:
        return redirect('inicio:registrate')

def moda_views(request):
    tipo = request.GET.get('tipo','')
    if tipo != '':
        articulo = electronicomodel.objects.obtener_filtros(tipo)
        paginator = Paginator(articulo, 40)
        num_page = request.GET.get('page')
        page = paginator.get_page(num_page) 
        return render(request, 'listar_moda.html', {'page':page})
    else:
        articulo = electronicomodel.objects.filter(categoria__id='5').exclude(id__in=[24,29])
        paginator = Paginator(articulo, 40)
        num_page = request.GET.get('page')
        page = paginator.get_page(num_page) 
        return render(request, 'listar_moda.html', {'page':page})
         

    


