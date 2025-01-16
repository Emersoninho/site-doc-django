from django.db import models

class Question(models.Model):
    question_text = models.CharField('pergunta', max_length=200)
    pub_date = models.DateTimeField('data de publicação')

    class Meta:
        verbose_name = 'pergunta'
        verbose_name_plural = 'perguntas'

    def __str__(self):
        return self.question_text
    
    def get_total_votes(self):
        votes = Choice.objects.filter(question=self).aggregate(total=models.sum('votes'))

        return votes.get('total')

    def get_results(self):
        total_votes = self.get_total_votes()
        votes = []
        for choice in self.choice_set.all():
            percentage = 0
            if choice.votes > and total_votes > 0:
                percentage = choice.votes / total_votes * 100

            votes.append({
                'text': choice.choice_text,
                'votes': choice.votes,
                'percentage':round(percentage, 2)
            })    

        return votes    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
