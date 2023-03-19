from django import forms
from inicio.models import electronicomodel

class electronicoform(forms.ModelForm):
    def __init__(self, pk, *args, **kwargs):
       
        super(electronicoform, self).__init__(*args, **kwargs)
        self.id_user = pk
   
    class Meta:
        model = electronicomodel
        fields = ('cantidad',)

   
    def clean_rating(self):
        cantidad = self.cleaned_data['cantidad']    
        articulo = self.id_user
        articulos = electronicomodel.objects.filter(id=articulo)
        if int(cantidad) > articulos.rating:
            return self.add_error('cantidad','no hay esta cantidad')
        else:
               return cantidad 