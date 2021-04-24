from django.urls import path
from .views import (
    ListQuestionView,
    CreateQuestionView,
    UpdateQuestionView,
    DeleteQuestionView,
)

app_name = 'tags'
urlpatterns = [
    path('', ListQuestionView.as_view(), name='list_questions'),
    path('create/', CreateQuestionView.as_view(), name='create_question'),
    path('update/<int:pk>/', UpdateQuestionView.as_view(), name='update_question'),
    path('delete/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
]
