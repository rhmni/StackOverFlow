from rest_framework import serializers
from app_comment.serializers import CommentSerializers
from .models import Answer


class AnswerSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializers(instance=comments, many=True).data

    class Meta:
        model = Answer
        fields = '__all__'
