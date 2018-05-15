from rest_framework import generics

from books import models
from . import serializers


class BookAPIView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
