from django.urls import path

from app_tag.views import ListTagView

app_name = 'tags'

urlpatterns = [
    path('', ListTagView.as_view(), name='list_tags'),
]
