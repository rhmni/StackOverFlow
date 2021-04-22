from rest_framework import serializers
from .models import Comment, Answer


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AnswerSerializers(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializers(instance=comments, many=True).data

    class Meta:
        model = Answer
        fields = '__all__'
