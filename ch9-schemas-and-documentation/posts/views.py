from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics

from . import models
from . import permissions
from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthorOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


# class PostList(generics.ListAPIView):
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthorOrReadOnly,)
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer


# class UserList(generics.ListAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = serializers.UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = serializers.UserSerializer
