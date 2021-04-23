from django.urls import path
from .views import BookmarkListView

app_name = 'bookmarks'
urlpatterns = [
    path('', BookmarkListView.as_view(), name='list_bookmarks'),
]
