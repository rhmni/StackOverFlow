from django.urls import path
from .views import BookmarkListView, QuestionListView
app_name = 'tags'

urlpatterns = [
    path('bookmarks/', BookmarkListView.as_view(), name='list_bookmarks'),
    path('', QuestionListView.as_view(), name='list_questions'),
]
