from django.shortcuts import render
from django.http import HttpResponse

# Define um view baseada em função
def index(request):
    # Retorne uma resposta HTTP
    return HttpResponse('Olá Django - index')

def ola(request):
    return HttpResponse('Olá Django')
