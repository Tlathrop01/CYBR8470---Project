from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm, ChoiceForm


#Basic landing page on login
@login_required
def profile(request):
    return render(request, 'CPApi/profile.html')

#index page view displays list of quesitons from the community
class IndexView(generic.ListView):
    template_name = "CPApi/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        #Returns the five most recently published issues
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

#This is the view used on addquestion.html to handle POSTing of new questions by users.
def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            Question = form.save(commit=False)
            Question.owner = request.user
            Question.pub_date = timezone.now()
            Question.save()
    form = QuestionForm()
    return render(request, "CPApi/addquestion.html", {"form": form})


#just used to render the base style for the website
def base(request):
    return render(request, "CPApi/base.html")

#Honest nothing ignore
@api_view(['GET'])
def rest_get_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    except Question.DoesNotExist:
        return Response({'error': 'Quesiton not found.'}, status=status.HTTP_404_NOT_FOUND)

#view for the detail page
class DetailView(generic.DetailView):
    model = Question
    template_name = "CPApi/detail.html"

#view to detail each quesitons results
class ResultsView(generic.DetailView):
    model = Question
    template_name = "CPApi/results.html"

#Votes for an issues will raise by 1 when someone selects as a choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "CPApi/detail.html",
            {
                #When a choice isn't selected this message displays
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        #Increments the vote by 1
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("CPApi:results", args=(question.id,)))