from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question
from .serializers import QuestionSerializer


class ListQuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class CreateQuestionView(APIView):
    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateQuestionView(APIView):
    def patch(self, request, pk):
        answer = get_object_or_404(Question, pk=pk)
        srz_data = QuestionSerializer(instance=answer, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteQuestionView(APIView):
    def delete(self, request, pk):
        answer = get_object_or_404(Question, pk=pk)
        answer.delete()
        return Response(data={'message': 'answer deleted successfully!'}, status=status.HTTP_200_OK)



