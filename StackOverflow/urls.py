from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('tags/', include('app_tag.urls', namespace='tags')),
    path('comments/', include('app_comment.urls', namespace='comments')),
    path('bookmarks/', include('app_bookmark.urls', namespace='bookmarks')),
    path('answers/', include('app_answer.urls', namespace='answers')),
    path('questions/', include('app_question.urls', namespace='questions')),
    path('users/', include('app_user.urls', namespace='users')),
]
