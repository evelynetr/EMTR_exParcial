from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki,articuloWiki

listaTemas = []

# Create your views here.
def index(request):
    return render(request, 'index.html',{
        'temaTodos':temaWiki.objects.all()
    })

def creaTema(request):
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        temaWiki.objects.create(
            nombreTema=nombreTema,
            descripcionTema=descripcionTema
        )
        return HttpResponseRedirect(reverse('wikiApp:creaTema'))
    return render(request,'creaTema.html',{
        'temaTodos':temaWiki.objects.all() 
    })

def creaArticulo(request):
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaRelacionado = request.POST.get('temaRelacionado')
        temaObj = temaWiki.objects.get(id=temaRelacionado)
        articuloWiki.objects.create(
            tituloArticulo=tituloArticulo,
            contenidoArticulo=contenidoArticulo,
            temaRelacionado=temaObj
        )
        return HttpResponseRedirect(reverse('wikiApp:creaArticulo'))
    return render(request, 'creaArticulo.html',{
        'temaTodos':temaWiki.objects.all()
    })

def listaArticuloPorTema(request,idTema):
    temaInfo = temaWiki.objects.get(id=idTema)
    listaArticulos = temaInfo.articulowiki_set.all()
    return render(request, 'listaArticuloPorTema.html',{
        'objTema':temaInfo,
        'listaArticulos':listaArticulos,
        'temaTodos':temaWiki.objects.all()
    }) 

def verArticulo(request,idArticulo):
    articuloInfo = articuloWiki.objects.get(id=idArticulo)
    return render(request, 'verArticulo.html',{
        'objArticulo': articuloInfo,
        'temaTodos':temaWiki.objects.all()
    })

def busqueda(request, palabraBusq):
    if request.method == 'POST':
        palabraBusq = request.POST.get('bsqArticulo')
        """return HttpResponseRedirect(reverse('wikiApp:busqueda palabraBusq '))"""
        return render(request, 'busqueda.html',{
            'palabraBusq':palabraBusq,
            'listaArticulos':articuloWiki.objects.all(),
            'temaTodos':temaWiki.objects.all() 
        }) 
    return render(request, 'busqueda.html',{
        'temaTodos':temaWiki.objects.all() 
    }) 

