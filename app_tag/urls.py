from django.urls import path
from app_tag.views import (
    ListTagView,
    CreateTagView,
    UpdateTagView,
    DeleteTagView
)

app_name = 'tags'

urlpatterns = [
    path('', ListTagView.as_view(), name='list_tags'),
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('update/<int:pk>/', UpdateTagView.as_view(), name='update_tag'),
    path('delete/<int:pk>/', DeleteTagView.as_view(), name='delete_tag'),
]
