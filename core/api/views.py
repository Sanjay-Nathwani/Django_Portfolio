from core.models import Question
from .serializers import QuestionSerializer

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def votingData(request):
    questions = Question.objects.all()

    backend = Question.objects.filter(answer='backend').count()
    frontend = Question.objects.filter(answer='frontend').count()
    fullstack = Question.objects.filter(answer='fullstack').count()

    # serializer = QuestionSerializer(questions,many=True)
    return Response({'backend':backend , 'frontend':frontend , 'fullstack':fullstack})