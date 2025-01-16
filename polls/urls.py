from django.urls import path
from polls.views import index, ola, question_create, question_update, question_delete, vote, results
from polls import views

urlpatterns = [
    path('index/', index, name='index'),
    path('ola/', ola, name='ola'),
    path('pergunta_create/', question_create, name='poll_create'),
    path('pergunta/<int:question_id>/', question_update, name='question_update'),
    path('pergunta/<int:question_id>/remove/', question_delete, name='question_remove'),
    # rota baseada em classe pk obrigatorio
    path('enquete/<int:pk>/show/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('enquete/list/', views.QuestionListView.as_view(), name='polls_list'),
    path('about-us/', views.SobreTemplateView.as_view(), name='about_page'),
    # baseada em função
    path('enquete/<int:question_id>/vote/', views.vote, name='poll_vote'),
    path('enquete/<int:question_id>/results/', views.results, name='poll_results'),
]
