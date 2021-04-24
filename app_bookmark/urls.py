from django.urls import path
from .views import (
    ListBookmarkView,
    CreateBookmarkView,
    UpdateBookmarkView,
    DeleteBookmarkView,
)

app_name = 'bookmarks'
urlpatterns = [
    path('', ListBookmarkView.as_view(), name='list_bookmarks'),
    path('create/', CreateBookmarkView.as_view(), name='create_bookmark'),
    path('update/<int:pk>/', UpdateBookmarkView.as_view(), name='update_bookmark'),
    path('delete/<int:pk>/', DeleteBookmarkView.as_view(), name='delete_bookmark'),
]
