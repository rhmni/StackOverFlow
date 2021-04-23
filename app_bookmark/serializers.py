from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = '__all__'
