from django.urls import path
from polls.views import index, ola, question_create, question_update

urlpatterns = [
    path('index/', index, name='index'),
    path('ola/', ola, name='ola'),
    path('pergunta_create/', question_create, name='poll_create'),
    path('pergunta/<int:question_id>/', question_update, name='question_update'),
]
