from django.urls import path
from .views import QuestionListView

app_name = 'tags'
urlpatterns = [
    path('', QuestionListView.as_view(), name='list_questions'),
]
