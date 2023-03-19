from carro_compra.models import carro_compras
from django.db.models import Sum, F
from django.shortcuts import redirect

def procesor_context(request):
    if request.user.is_authenticated:
        numero = carro_compras.objects.filter(user=request.user).count()
        tota = carro_compras.objects.aggregate(total = Sum( F('cantidad')*F('productos__precio')))
        if tota is not None:
            return {
                'numero':numero,
                'valor':tota
            }
        else:
            return {
                'numero':numero,
                'valor':0
            }
    else:
        return {}
    
       