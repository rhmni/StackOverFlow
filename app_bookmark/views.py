from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bookmark
from .serializers import BookmarkSerializer
from permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ListBookmarkView(APIView):
    def get(self, request):
        bookmarks = Bookmark.objects.all()
        srz_data = BookmarkSerializer(instance=bookmarks, many=True)
        return Response(srz_data.data, status=status.HTTP_200_OK)


class CreateBookmarkView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        srz_data = BookmarkSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateBookmarkView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def patch(self, request, pk):
        bookmark = get_object_or_404(Bookmark, pk=pk)
        self.check_object_permissions(request, bookmark)
        srz_data = BookmarkSerializer(instance=bookmark, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookmarkView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        bookmark = get_object_or_404(Bookmark, pk=pk)
        self.check_object_permissions(request, bookmark)
        bookmark.delete()
        return Response(data={'message': 'bookmark deleted successfully!'}, status=status.HTTP_200_OK)
