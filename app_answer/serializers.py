from rest_framework import serializers
from app_comment.serializers import CommentSerializer
from .models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(instance=comments, many=True).data

    class Meta:
        model = Answer
        fields = '__all__'
