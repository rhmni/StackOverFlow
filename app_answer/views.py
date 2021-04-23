from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer
from .serializers import AnswerSerializers


class AnswerListView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        srz_data = AnswerSerializers(instance=answers, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
