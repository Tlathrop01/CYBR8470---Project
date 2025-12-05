import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        #test for the Question published recently function
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        #test for old questions
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        #test for new questions
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    #Creates an issue for testing purposes
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

#Tests the question created
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        #Tests if no issues present  and verifies the list of issues
        response = self.client.get(reverse("CPApi:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No issues are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        #Issues with a past pub_date are displayed
        question = create_question(question_text="Past issue.", days=-30)
        response = self.client.get(reverse("CPApi:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        #Issues with a future pub_date are displayed
        create_question(question_text="Future issue.", days=30)
        response = self.client.get(reverse("CPApi:index"))
        self.assertContains(response, "No issues are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        #Displays past issues
        question = create_question(question_text="Past issue.", days=-30)
        create_question(question_text="Future issue.", days=30)
        response = self.client.get(reverse("CPApi:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        #Allows the display of multiple issues
        question1 = create_question(question_text="Past issue 1.", days=-30)
        question2 = create_question(question_text="Past issue 2.", days=-5)
        response = self.client.get(reverse("CPApi:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )