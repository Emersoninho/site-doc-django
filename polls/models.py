from django.db import models

class Question(models.Model):
    question_text = models.CharField('pergunta', max_length=200)
    pub_date = models.DateTimeField('data de publicação')

    class Meta:
        verbose_name = 'pergunta'
        verbose_name_plural = 'perguntas'
