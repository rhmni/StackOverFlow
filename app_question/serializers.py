from rest_framework import serializers

from app_bookmark.serializers import BookmarkSerializer
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    bookmarks = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answers = obj.answers.all()
        return BookmarkSerializer(instance=answers, many=True).data

    def get_bookmarks(self, obj):
        bookmarks = obj.bookmarks.all()
        return BookmarkSerializer(instance=bookmarks, many=True).data

    class Meta:
        model = Question
        fields = '__all__'
