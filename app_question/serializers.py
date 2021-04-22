from rest_framework import serializers
from .models import Question, Bookmark


class BookmarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'


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
