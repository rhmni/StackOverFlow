from .models import Tag
from .serializers import TagSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ListTagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        srz_data = TagSerializer(instance=tags, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)


class CreateTagView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        srz_data = TagSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTagView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def patch(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        self.check_object_permissions(request, tag)
        srz_data = TagSerializer(instance=tag, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTagView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        self.check_object_permissions(request, tag)
        tag.delete()
        return Response(data={'message': f'tag {tag.name} deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
