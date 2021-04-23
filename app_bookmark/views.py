from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bookmark
from .serializers import BookmarkSerializers


class BookmarkListView(APIView):
    def get(self, request):
        bookmarks = Bookmark.objects.all()
        srz_data = BookmarkSerializers(instance=bookmarks, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)
