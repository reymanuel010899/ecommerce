from django.db import models
from django.contrib.auth.models import User
from .manayer import card_chopmanayer
from inicio.models import electronicomodel
ALMACENAR=(
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256')
)

# Create your models here.

        
class carro_compras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    productos = models.ForeignKey(electronicomodel, related_name='carro_devolver', blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    objects = card_chopmanayer()
    created = models.DateTimeField(auto_now_add=True)       

    def __str__(self) -> str:
        return str(self.id)+ '-' +  self.productos.titulo

    class Meta:
        unique_together = ('user','productos')


    