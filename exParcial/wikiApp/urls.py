from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('creaTema',views.creaTema,name='creaTema'),
    path('creaArticulo',views.creaArticulo,name='creaArticulo'),
    path('listaArticuloPorTema/<str:idTema>',views.listaArticuloPorTema,name='listaArticuloPorTema'),
    path('verArticulo/<str:idArticulo>',views.verArticulo,name='verArticulo'),
    path('busqueda/<str:palabraBusq>',views.busqueda,name='busqueda')  
]
