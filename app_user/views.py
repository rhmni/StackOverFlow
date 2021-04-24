from django.shortcuts import get_object_or_404
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


class CreateQuestionView(APIView):
    def post(self, request):
        srz_data = UserSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateQuestionView(APIView):
    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        srz_data = UserSerializer(instance=user, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteQuestionView(APIView):
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(data={'message': 'user deleted successfully!'}, status=status.HTTP_200_OK)


