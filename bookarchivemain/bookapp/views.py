from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from bookapp.models import *
from django.contrib.auth.views import LoginView
from django.utils import timezone
from django.views.generic import ListView, DeleteView
from bookapp.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied


# Create your views here.
def books(request):
    outbooks = Books.objects.all()
    numbers = list(range(1, 6))
    for book in outbooks:
        ratings = Rating.objects.filter(book=book)
        total_rating = 0
        num_ratings = 0
        for rating in ratings:
            total_rating += rating.rating_value
            num_ratings += 1
        avg_rating = round(total_rating / num_ratings, 1) if num_ratings > 0 else 0
        book.avg_rating = avg_rating
    data = {
        'object_list': outbooks,
        'numbers': numbers,
    }
    return render(request, 'bookapp/books.html', data)


def booksinside(request, book_id):
    book = Books.objects.filter(id=book_id)
    parts = Parts.objects.filter(book=book_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            if request.user.id == None:
                return redirect('login')
            else:
                user_id = request.user.id
                rating_value = form.cleaned_data['rating_value']
                rating = Rating(rating_value=rating_value, book_id=book_id, user_id=user_id)
                existing_rating = Rating.objects.filter(user=request.user.id, book_id=book_id).first()
                if existing_rating:
                    existing_rating.rating_value = rating_value
                    existing_rating.save()
                else:
                    rating.save()
                return redirect('books')
        else:
            form = RatingForm()
    data = {
        'books': book,
        'parts': parts,
    }
    return render(request, 'bookapp/currentbook.html', data)


def read_part(request, parts_id):
    books = Books.objects.filter()
    test_parts = Parts.objects.get(id=parts_id)
    author = test_parts.book.author
    parts = Parts.objects.filter(id=parts_id)
    comments = Comments.objects.filter(part_id=parts_id)
    comments = comments.order_by('-comment_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.id == None:
                return redirect('login')
            else:
                comment_text = form.cleaned_data['comment_text']
                comment_author = request.user.id
                comment = Comments(comment_text=comment_text, comment_author_id=comment_author, part_id=parts_id)
                comment.save()
                return redirect('read', parts_id)
        else:
            form = CommentForm()

    data = {
        'author': author,
        'parts': parts,
        'books': books,
        'comments': comments,
    }
    return render(request, 'bookapp/read.html', data)


def create_glava(request, id):
    if request.method == 'POST':
        form = PartsForm(request.POST)
        if form.is_valid():
            book_id = id
            part_name = form.cleaned_data['part_name']
            part_content = form.cleaned_data['part_content']
            book = Parts(part_name=part_name, part_content=part_content, book_id=book_id)
            book.save()
            return redirect('lk')
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
            return redirect('login')
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
    return redirect('/')


def edit_part(request, parts_id, id):
    part_get = get_object_or_404(Parts, id=parts_id)
    books = get_object_or_404(Books, id=id, author=request.user)
    myupdate = PartsForm(instance=part_get)
    if request.method == 'POST':
        form = PartsForm(request.POST, instance=part_get)
        if form.is_valid():
            form.save()
            return redirect('lk')
        else:
            form = PartsForm()
    data = {
        'partshow': part_get,
        'showbooks': books,
        'form': myupdate,
    }
    return render(request, 'bookapp/editglava.html', data)


def lk(request):
    if request.user.id == None:
        raise PermissionDenied()
    else:
        books = Books.objects.filter(author=request.user.id)
        data = {
            'showbooks': books,
        }
        return render(request, 'bookapp/lk.html', data)


def genres(request, id):
    outbooks = Books.objects.filter(genres=id)
    numbers = list(range(1, 6))
    for book in outbooks:
        ratings = Rating.objects.filter(book=book)
        total_rating = 0
        num_ratings = 0
        for rating in ratings:
            total_rating += rating.rating_value
            num_ratings += 1
        avg_rating = round(total_rating / num_ratings, 1) if num_ratings > 0 else 0
        book.avg_rating = avg_rating
    data = {
        'object_list': outbooks,
        'numbers': numbers,
    }
    return render(request, 'bookapp/books.html', data)


def createbook(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            author_id = request.user.id
            book_name = form.cleaned_data['book_name']
            book_description = form.cleaned_data['book_description']
            book_status = form.cleaned_data['book_status']
            book_img = form.cleaned_data['book_img']
            book = Books(book_name=book_name, book_description=book_description, author_id=author_id,
                         book_status=book_status, book_img=book_img)
            book.save()
            book.genres.set(form.cleaned_data['genres'])
            book.save()
            return redirect('lk')
        else:
            form = BooksForm()
    books = Books.objects.all()
    genres = Genres.objects.all()
    status = Status.objects.all()
    data = {
        'books': books,
        'genres': genres,
        'status': status,
    }
    return render(request, 'bookapp/createbook.html', data)


def profile_setup(request):
    if request.user.id == None:
        raise PermissionDenied()
    else:
        users_get = get_object_or_404(get_user_model(), id=request.user.id)
        form = SettingsForm(instance=users_get)
        if request.method == 'POST':
            myform = SettingsForm(request.POST, request.FILES, instance=users_get)
            if myform.is_valid():
                myform.save()
                redirect('profile_setup')
            else:
                myform = SettingsForm()
        data = {
            'form': form,
        }
        return render(request, 'bookapp/profile_settings.html', data)


class DeleteBookView(DeleteView):
    model = Books
    template_name = 'bookapp/delete_book.html'
    success_url = reverse_lazy('lk')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.author.id != self.request.user.id:
            raise PermissionDenied("You are not the author of this book")
        return obj


class DeletePartView(DeleteView):
    model = Parts
    template_name = 'bookapp/delete_part.html'
    success_url = reverse_lazy('lk')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.book.author.id != self.request.user.id:
            raise PermissionDenied("You are not the author of this book")
        return obj


def edit_book(request, pk):
    books = get_object_or_404(Books, id=pk, author=request.user)
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES, instance=books)
        if form.is_valid():
            form.save()  # Save the form instance, no need to create a new book object
            return redirect('lk')
    else:
        form = BooksForm()
    genres = Genres.objects.all()
    status = Status.objects.all()
    data = {
        'books': books,
        'genres': genres,
        'status': status,
    }
    return render(request, 'bookapp/editbook.html', data)


class SearchView(ListView):
    model = Books
    template_name = 'bookapp/books.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Books.objects.filter(
            Q(book_name__icontains=query)
        )
        return object_list


def report_comment(request, part_id, pk):
    report_object = Reports.objects.filter(comment_id=pk)
    comments = Comments.objects.filter(id=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.report_author = request.user
            report.comment = comments.first()
            report.save()
            return redirect('read', part_id)
    else:
        form = ReportForm()
    data = {
        'reports':report_object,
        'form': form,
        'comments':comments,
    }
    return render(request, 'bookapp/report_comment_page.html', data)

def report_book(request, pk):
    report_object = Reports.objects.filter(comment_id=pk)
    books = Books.objects.filter(id=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.report_author = request.user
            report.book = books.first()
            report.save()
            return redirect('insidebook', pk)
    else:
        form = ReportForm()
    data = {
        'reports':report_object,
        'form': form,
        'books':books,
    }
    return render(request, 'bookapp/report_page.html', data)