import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Issue(models.Model):
    Issue_name = models.CharField(max_length=25)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text