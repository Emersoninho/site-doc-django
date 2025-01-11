from django.urls import path
from polls.views import index, ola, question_create

urlpatterns = [
    path('index/', index, name='index'),
    path('ola/', ola, name='ola'),
    path('pergunta_create/', question_create, name='poll_create'),
]
