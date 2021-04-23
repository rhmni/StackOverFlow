from rest_framework import serializers
from app_answer.serializers import AnswerSerializers
from app_bookmark.serializers import BookmarkSerializers
from app_comment.serializers import CommentSerializers
from app_question.serializers import QuestionSerializers
from app_user.models import User


class UserSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()
    bookmarks = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializers(instance=comments, many=True).data

    def get_questions(self, obj):
        questions = obj.questions.all()
        return QuestionSerializers(instance=questions, many=True).data

    def get_bookmarks(self, obj):
        bookmarks = obj.bookmarks.all()
        return BookmarkSerializers(instance=bookmarks, many=True).data

    def get_answers(self, obj):
        answers = obj.answers.all()
        return AnswerSerializers(instance=answers, many=True).data

    class Meta:
        model = User
        fields = '__all__'
