from django.db import models
from app_tag.models import Tag
from app_user.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=250)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='questions')
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='bookmarks')
    create_date = models.DateTimeField()

    def __str__(self):
        return self.question.title



