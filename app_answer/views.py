from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app_answer.models import Comment, Answer
from app_answer.serializers import CommentSerializers, AnswerSerializers


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        srz_data = CommentSerializers(instance=comments, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class AnswerListView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        srz_data = AnswerSerializers(instance=answers, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
