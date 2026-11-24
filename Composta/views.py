from django.shortcuts import render

def inicio(request):
    return render (request, 'Composta/incio.html')
def pasos(request):
    return render(request, 'Composta/pasos.html')


# Create your views here.
