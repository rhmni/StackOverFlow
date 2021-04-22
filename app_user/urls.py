from django.urls import path

from .views import ListUserView

app_name = 'users'

urlpatterns = [
    path('', ListUserView.as_view(), name='list_users'),
]
