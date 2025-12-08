from django.urls import path
from CPApi.views import rest_get_question, profile, addquestion, base

from . import views

#they're urls
app_name = "CPApi"
urlpatterns = [
    path("", base, name="base"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('rest/question/<int:question_id>/', rest_get_question, name='rest_get_question'),
    path('profile/', profile, name='profile'),
    path('account/addquestion/', addquestion, name='addquestion'),
]