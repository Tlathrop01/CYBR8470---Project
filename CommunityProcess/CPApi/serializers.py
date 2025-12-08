from rest_framework import serializers
from .models import Question

#could be useful if I were devloping based this class
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'owner', 'question_text', 'pub_date']