from django.contrib import admin
from django.urls import path
from book_api.views import BookList, BookCreate, Book_Detail
urlpatterns = [
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>/', Book_Detail.as_view())
]
