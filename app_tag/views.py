from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag
from .serializers import TagSerializer
from rest_framework import status


class ListTagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        srz_data = TagSerializer(instance=tags, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
