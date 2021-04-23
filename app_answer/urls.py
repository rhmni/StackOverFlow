from django.urls import path
from .views import AnswerListView

app_name = 'tags'

urlpatterns = [
    path('', AnswerListView.as_view(), name='list_answers'),
]
