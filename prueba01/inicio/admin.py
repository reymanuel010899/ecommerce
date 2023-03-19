from django.contrib import admin
from .models import celularesmodels, laptopmodels, acesoriomodels, monitoresmodels, cpumodels, tablesmodels, electronicomodel,categoria, vistas, ofertas_descuentos

class ConfigugarElectronic(admin.ModelAdmin):
    search_fields = ('modelo',)

admin.site.register(electronicomodel, ConfigugarElectronic)
admin.site.register(categoria)
admin.site.register(celularesmodels)
admin.site.register(laptopmodels)
admin.site.register(acesoriomodels)
admin.site.register(monitoresmodels)
admin.site.register(cpumodels)
admin.site.register(tablesmodels)
admin.site.register(vistas)
admin.site.register(ofertas_descuentos)



