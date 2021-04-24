from django.urls import path
from .views import (
    ListAnswerView,
    CreateAnswerView,
    UpdateAnswerView,
    DeleteAnswerView,
)

app_name = 'tags'

urlpatterns = [
    path('', ListAnswerView.as_view(), name='list_answers'),
    path('create/', CreateAnswerView.as_view(), name='create_answer'),
    path('update/<int:pk>/', UpdateAnswerView.as_view(), name='update_answer'),
    path('delete/<int:pk>/', DeleteAnswerView.as_view(), name='delete_answer'),
]
