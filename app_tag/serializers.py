from rest_framework import serializers
from app_tag.models import Tag
from app_user.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        users = obj.users.all()
        return UserSerializer(instance=users, many=True).data

    class Meta:
        model = Tag
        fields = '__all__'
