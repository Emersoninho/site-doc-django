from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.contrib.auth.decorators import login_required

# Define um view baseada em função
def index(request):
    # Retorne uma resposta HTTP
    #return HttpResponse('Olá Django - index')
    #return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'bem bindo ao sistema de Enquetes'})

@login_required
def ola(request):
    #return HttpResponse('Olá Django')
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'polls/questions.html', context)