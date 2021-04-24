from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Answer
from .serializers import AnswerSerializer


class ListAnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        srz_data = AnswerSerializer(instance=answers, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class CreateAnswerView(APIView):
    def post(self, request):
        srz_data = AnswerSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateAnswerView(APIView):
    def patch(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        srz_data = AnswerSerializer(instance=answer, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAnswerView(APIView):
    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        answer.delete()
        return Response(data={'message': 'answer deleted successfully!'}, status=status.HTTP_200_OK)
