from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializers


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        srz_data = CommentSerializers(instance=comments, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
