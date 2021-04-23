from rest_framework import serializers

from app_bookmark.serializers import BookmarkSerializers
from .models import Question


class QuestionSerializers(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    bookmarks = serializers.SerializerMethodField()

    def get_answers(self, obj):
        answers = obj.answers.all()
        return BookmarkSerializers(instance=answers, many=True).data

    def get_bookmarks(self, obj):
        bookmarks = obj.bookmarks.all()
        return BookmarkSerializers(instance=bookmarks, many=True).data

    class Meta:
        model = Question
        fields = '__all__'
