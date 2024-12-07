from django.urls import path
from . import views

app_name='wikiApp' 

urlpatterns = [
    path('',views.index,name='index'),
    path('creaTema',views.creaTema,name='creaTema'),
    path('creaArticulo',views.creaArticulo,name='creaArticulo'),
    path('listaArticuloPorTema',views.listaArticuloPorTema,name='listaArticuloPorTema'),
    path('listaArticulo',views.listaArticulo,name='listaArticulo'),
    path('busqueda',views.busqueda,name='busqueda'),
]
