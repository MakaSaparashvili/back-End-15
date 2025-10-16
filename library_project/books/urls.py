from django.urls import path
from .views import book_list, BookDetailView

urlpatterns = [
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
