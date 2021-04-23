from django.db import models
from app_answer.models import Answer
from app_user.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.text
