from django.urls import path

from .views import (
    ListUserView,
    CreateUserView,
    UpdateUserView,
    DeleteUserView,
)

app_name = 'users'

urlpatterns = [
    path('', ListUserView.as_view(), name='list_users'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('update/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
]
