from django.db import models
from app_question.models import Question
from app_user.models import User


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.text


