from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app_user.models import User
from app_user.serializers import UserSerializer


class ListUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserSerializer(instance=users, many=True)
        return Response(data=srz_data.data, status=status.HTTP_200_OK)
