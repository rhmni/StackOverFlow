from django.urls import path
from .views import (
    CommentListView,
)

app_name = 'comments'
urlpatterns = [
    path('', CommentListView.as_view(), name='list_comments'),
]
