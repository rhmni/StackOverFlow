from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question
from .serializers import QuestionSerializers


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializers(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)



