from django.urls import path
from .views import CommentListView, AnswerListView

app_name = 'tags'

urlpatterns = [
    path('comments/', CommentListView.as_view(), name='list_comments'),
    path('', AnswerListView.as_view(), name='list_answers'),
]
