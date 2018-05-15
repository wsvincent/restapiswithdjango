from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view()),
]
