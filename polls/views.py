from django.shortcuts import render, redirect, get_object_or_404
from polls.models import Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from polls.forms import QuestionForm
from django.urls import reverse_lazy

def index(request):
    aviso = 'Aviso Importante: esta página não exige login'
    messages.warning(request, aviso)
    questions = Question.objects.all()
    context = {'all_question': questions, 'titulo': 'ultimas enquetes'}
    return render(request, 'index.html', context)

@login_required
def ola(request):
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'polls/questions.html', context)

@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] = form
    context['form_title'] = 'Criando uma pergunta'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta criada com sucesso.')
            return redirect('index')
        
    return render(request, 'polls/question_form.html', context)   

@login_required
def question_update(request, question_id):
    context = {}
    question = get_object_or_404(Question, id=question_id)
    form = QuestionForm(request.POST or None, instance=question)
    context['form'] = form
    context['form_title'] = 'Editando a pergunta'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta criada com sucesso.')
            return redirect('index')

    return render(request, 'polls/question_form.html', context) 

@login_required
def question_delete(request, question_id):
    context = {}
    question = get_object_or_404(Question, id=question_id)
    context['object'] = question
    
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Pergunta excluida com sucesso.')
        return redirect('index')
    
    return render(request, 'polls/question_confirm_delete_form.html', context)