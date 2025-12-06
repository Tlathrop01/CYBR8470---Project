import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Currently useless model made for future 
class Issue(models.Model):
    Issue_name = models.CharField(max_length=25)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
# This represents the current issue handling for the app I just can't be bothered to change the name yet
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# These are the choices for each issue(Question) 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text