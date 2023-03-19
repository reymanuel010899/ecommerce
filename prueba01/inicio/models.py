from django.db import models
from django.contrib.auth.models import User
from .maneger import categora_manayer, ofertas_manayer,  VistaManayer
from django.db.models.signals import post_save
from PIL import Image
from .maneger import electronicomanayer

class categoria(models.Model):
    nombre = models.CharField(max_length=30)
    objects =categora_manayer()

    def __str__(self):
        return str(self.id) +'-'+ self.nombre

# Create your models here.

ALMACENAR=(
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256')
)

COLOR = (
    ('R','ROJO'),
    ('N','NEGRO'),
    ('B','BLANCO'),
    ('O','OTROS')
)

TIPO_ROPA = (('1','abrigo'),('2','pantalon'),('3','tenis'),('4','ropa interior'))
TIPO_SIZE = (('1','L'),('2','M'),('3','X'),('4','XL'))
TIPO_GENERO = (('2','mujer'),('3','niño'))
TIPO_ROPA_MUJER = (('1', 'vestido'),('2', 'zapatilla'),('3', 'ropa interior'), ('4','blusa'))

class electronicomodel(models.Model):
        objects = electronicomanayer()
        categoria = models.ForeignKey(categoria, related_name='categorias', blank=True, on_delete=models.CASCADE)
        size = models.CharField(max_length=1, blank=True, choices=TIPO_SIZE)
        tipo_ropa = models.CharField(max_length=1,blank=True, choices=TIPO_ROPA) 
        tipo_ropa_mujer = models.CharField(max_length=1, choices=TIPO_ROPA_MUJER, blank=True)
        tipa_genero =models.CharField(max_length=1, choices=TIPO_GENERO, blank=True)       
        titulo = models.CharField(max_length=300, blank=True)
        modelo = models.CharField(max_length=50, blank=True)
        marca = models.CharField(max_length=30, blank=True)
        avatar = models.FileField(upload_to='electronico', blank=True)
        imagen1 = models.ImageField(upload_to='ímagen', blank=True, null=True)
        imagen2 = models.ImageField(upload_to='ímagen', blank=True, null=True)
        imagen3 = models.ImageField(upload_to='ímagen', blank=True, null=True)
        imagen4 = models.ImageField(upload_to='ímagen', blank=True, null=True)
        procesador = models.CharField(max_length=50, blank=True) 
        precio = models.FloatField()
        in_portada = models.BooleanField(default=False)
        tipo = models.CharField(max_length=50, blank=True)
        tamaño = models.CharField(max_length=5, blank=True)
        cantidad = models.PositiveIntegerField(default=1 )
        detalles = models.TextField(blank=True)
        almacenamiento = models.CharField(max_length=3,blank=True, choices=ALMACENAR)
        rating = models.PositiveIntegerField( default=1,blank=True)
        created = models.DateTimeField(auto_now_add=True)

    

        def __str__(self) -> str:
            return str(self.id) + '-' + self.modelo

        def get_vistas_count(self):
            return self.devolver_views.all().count()
       


class vistas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    articulo = models.ForeignKey(electronicomodel, related_name='devolver_views',  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  
    objects = VistaManayer()

    def __str__(self) -> str:
        return str(self.id)+ '-' + self.user.username

    

class ofertas_descuentos(models.Model):
    titulo = models.TextField(max_length=500)
    porciento = models.IntegerField()
    descuentos = models.FloatField()
    producto = models.ForeignKey(electronicomodel, related_name='oferta_devolver', on_delete=models.CASCADE)
    in_port = models.BooleanField()
    objects = ofertas_manayer()
    created = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self) -> str:
        return str(self.id)+ '-' + self.titulo


class celularesmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='celular')
    titulo = models.CharField(max_length=300)
    modelo = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='celulares')   
    precio = models.CharField(max_length=5)
    detalles = models.TextField()
    almacenamiento = models.CharField(max_length=3, choices=ALMACENAR)
    color = models.CharField(max_length=10, choices=COLOR)
    rating = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.modelo





class laptopmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='laptop')
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='laptop')   
    precio = models.CharField(max_length=10)
    almacenamiento = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.modelo

class  acesoriomodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='acesorio')
    titulo = models.CharField(max_length=300)
    tipos = models.CharField(max_length=50) 
    detalle = models.TextField()
    avatar = models.FileField(upload_to='acesorios')   
    precio = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.tipos
class tablesmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='table')
    titulo = models.CharField(max_length=300)
    marca = models.CharField(max_length=30)
    avatar = models.FileField(upload_to='tables')   
    detalle = models.TextField()
    almacenamiento = models.CharField(max_length=30)
    precio = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.detalle
class monitoresmodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='monitores')
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='tables') 
    precio = models.CharField(max_length=10)
    detalle = models.TextField()
    tamaño = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.model
class cpumodels(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.ManyToManyField(electronicomodel, blank=True, related_name='cpu')
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    procesador = models.CharField(max_length=50)
    avatar = models.FileField(upload_to='tables') 
    precio = models.CharField(max_length=10)
    detalle = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    stok = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.model