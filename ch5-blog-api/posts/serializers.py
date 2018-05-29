from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = models.Post
