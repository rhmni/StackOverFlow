from rest_framework import serializers
from app_answer.serializers import AnswerSerializers
from app_bookmark.serializers import BookmarkSerializer
from app_comment.serializers import CommentSerializer
from app_question.serializers import QuestionSerializer
from app_user.models import User


class UserSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    bookmarks = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(instance=comments, many=True).data

    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionSerializer(instance=questions, many=True).data

    def get_bookmarks(self, obj):
        bookmarks = obj.bookmarks.all()
        return BookmarkSerializer(instance=bookmarks, many=True).data

    def get_answers(self, obj):
        answers = obj.answers.all()
        return AnswerSerializers(instance=answers, many=True).data

    class Meta:
        model = User
        fields = '__all__'
