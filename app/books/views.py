from django.shortcuts import render
from django.http import HttpResponse

from app.books.models import Book


# Create your views here.

def seeBooks(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})