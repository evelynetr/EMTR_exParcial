from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def creaTema(request):
    return render(request, 'creaTema.html')

def creaArticulo(request):
    return render(request, 'creaArticulo.html')

def listaArticuloPorTema(request):
    return render(request, 'listaArticuloPorTema.html')

def listaArticulo(request):
    return render(request, 'listaArticulo.html')

def busqueda(request):
    return render(request, 'busqueda.html')

