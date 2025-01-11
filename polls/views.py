from django.shortcuts import render, redirect
from polls.models import Question
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.views.generic.edit import CreateView
from polls.forms import QuestionForm
from django.urls import reverse_lazy

# Define um view baseada em função
def index(request):
    # Retorne uma resposta HTTP
    #return HttpResponse('Olá Django - index')
    #return render(request, 'index.html')
    aviso = 'Aviso Importante: esta página não exige login'
    messages.warning(request, aviso)
    return render(request, 'index.html', {'titulo': 'bem bindo ao sistema de Enquetes'})

@login_required
def ola(request):
    #return HttpResponse('Olá Django')
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'polls/questions.html', context)

# class QuestionCreateView(CreateView):
#     model = Question
#     template_name = 'polls/question_form.html'
#     fields = ('question_text', 'pub_date')
#     success_url = reverse_lazy('index')
#     success_message = 'Pergunta Crianda com Sucesso.'

#     def form_valid(self, form):
#         messages.success(self.request, self.success_message)
#         return super(QuestionCreateView).form_valid(form)

@login_required
def question_create(request):
    context = {}
    form = QuestionForm(request.POST or None, request.FILES or None)
    context['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Pergunta criada com sucesso.')
            return redirect('index')
        
    return render(request, 'polls/question_form.html', context)    