from django import forms
from polls.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
        widgets = {
            'pub_date': forms.DateInput(
                format= '%Y-%m-%d',
                attrs={'type': 'date'}
            ),
        }