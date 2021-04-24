from django.urls import path
from .views import (
    ListCommentView,
    CreateCommentView,
    UpdateCommentView,
    DeleteCommentView,
)

app_name = 'comments'
urlpatterns = [
    path('', ListCommentView.as_view(), name='list_comments'),
    path('create/', CreateCommentView.as_view(), name='create_comment'),
    path('update/<int:pk>/', UpdateCommentView.as_view(), name='update_comment'),
    path('delete/<int:pk>/', DeleteCommentView.as_view(), name='delete_comment'),
]
