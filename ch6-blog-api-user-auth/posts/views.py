from rest_framework import generics

from . import models
from . import permissions
from . import serializers


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthorOrReadOnly,)
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
