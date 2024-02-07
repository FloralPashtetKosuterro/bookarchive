from django.shortcuts import render, redirect, get_object_or_404
from bookapp.models import *
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.views.generic import ListView
from bookapp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied


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


def create_glava(request, id):
    if request.method == 'POST':
        form = PartsForm(request.POST)
        if form.is_valid():
            book_id = id
            part_name =form.cleaned_data['part_name']
            part_content =form.cleaned_data['part_content']
            book = Parts(part_name=part_name, part_content=part_content,book_id=book_id)
            book.save()
            return redirect('../books')
        else:
            form = PartsForm()
    parts = Parts.objects.all()
    books = get_object_or_404(Books, id=id, author=request.user)
    data = {
        'cycle': parts,
        'showbooks': books,
    }
    return render(request, 'bookapp/createglava.html', data)


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена!</h1>')


def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'bookapp/registration_done.html')
    else:
        form = RegForm()
    return render(request, 'bookapp/reg.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'bookapp/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('books')


def logout_view(request):
    logout(request)
    return redirect('/books')


def lk(request):
    books = Books.objects.filter(author=request.user.id)
    data = {
        'showbooks': books,
    }
    return render(request, 'bookapp/lk.html', data)


def events(request):
    return render(request, 'bookapp/limited_event.html')
