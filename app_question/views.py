from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Bookmark
from app_question.serializers import QuestionSerializers, BookmarkSerializers


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializers(instance=questions, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class BookmarkListView(APIView):
    def get(self, request):
        answers = Bookmark.objects.all()
        srz_data = BookmarkSerializers(instance=answers, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
