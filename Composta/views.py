from django.shortcuts import render

def inicio(request):
    return render (request, 'Composta/incio.html')
def pasos(request):
    return render(request, 'Composta/pasos.html')
def tipos(request):
    return render(request, 'Composta/tipos.html')

# Create your views here.
