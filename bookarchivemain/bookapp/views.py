from django.shortcuts import render, redirect
from bookapp.models import *
from django.utils import timezone
from django.views.generic import ListView
from bookapp.forms import *

# Create your views here.

def main(request):
    getitems = Categories.objects.all()
    getnews = News.objects.filter(news_time__lte=timezone.now()).order_by('-news_time')
    data = {
        'categoryshow': getitems,
        'news': getnews,
    }
    return render(request, 'bookapp/index.html', data)


def katalog(request):
    return render(request, 'bookapp/katalog.html')


def newbooks(request):
    return render(request, 'bookapp/newbooks.html')


def books(request):
    outbooks = Books.objects.all()
    data = {
        'bookshow': outbooks
    }
    return render(request, 'bookapp/books.html', data)


def booksinside(request, book_id):
    book = Books.objects.filter(id=book_id)
    parts = Parts.objects.filter(book=book_id)
    data = {
        'books': book,
        'parts': parts,
    }
    return render(request, 'bookapp/currentbook.html', data)


def create_glava(request):
    if request.method == 'POST':
        form = PartsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = PartsForm()
    parts = Parts.objects.all()
    books = Books.objects.all()
    data = {
        'cycle': parts,
        'showbooks':books,
    }
    return render(request, 'bookapp/createglava.html', data)


def events(request):
    return render(request, 'bookapp/limited_event.html')
