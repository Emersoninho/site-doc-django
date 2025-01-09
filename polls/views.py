from django.shortcuts import render
from django.http import HttpResponse

# Define um view baseada em função
def index(request):
    # Retorne uma resposta HTTP
    #return HttpResponse('Olá Django - index')
    #return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'bem bindo ao sistema de Enquetes'})

def ola(request):
    return HttpResponse('Olá Django')
