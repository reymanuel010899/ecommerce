from rest_framework.routers import DefaultRouter
from .views import grudview, categoria_view
app_name = 'tienda_api'

roters = DefaultRouter()

roters.register(r'grud-electrodomestico/', grudview, basename='grud-electrodomestico')
roters.register(r'api-categoria/', categoria_view , basename='categoria')

urlpatterns = roters.urls