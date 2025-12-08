from django import forms
from .models import Question, Choice


#Contains the box used on addquestion.html to submit questions (dunno why the widget doesn't work dont ask)
class QuestionForm(forms.ModelForm):
    body = Question.question_text
    Question.question_text = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Ask a question...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Question
        exclude = ("owner", "pub_date" )

#choices for adding to questions
class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        exclude = ("question_id", "votes")