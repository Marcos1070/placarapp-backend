from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, CategoriaViewSet, SucursalViewSet

#instanciamos el router por defecto de DRF
router = DefaultRouter()



#registramos nuestros ViewSets con un prefijo para la URL
router.register(r'clientes', ClienteViewSet, basename = 'cliente')
router.register(r'categorias', CategoriaViewSet, basename = 'categorias')
router.register(r'sucursales', SucursalViewSet, basename = 'sucursal')


# las urls de la api se generan automaticamente a partir del router
urlpatterns = [

    path('', include(router.urls))

]

