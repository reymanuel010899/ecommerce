from django.db import models
from django.db.models import Count, Sum, F



class card_chopmanayer(models.Manager):
    def cantidad_producto(self):
        numero = self.all()
        cantidad = self.aggregate(num_productos = Count(numero)) 
        return cantidad

   

 
    def cantidad_total(self):
        return filter(user='2').aggregate(nun=Sum('productos__precio'))
            