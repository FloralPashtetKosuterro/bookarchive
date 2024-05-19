from django import forms

from . import views
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .views import *
from django.contrib.auth import authenticate


class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = ['part_name', 'part_content']
    #
    # def __init__(self, **kwargs):
    #     super(PartsForm, self).__init__(**kwargs)
    #     if ['book',]:
    #         self.fields['book'].queryset = Books.objects.filter(author=id)


class RegForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'nickname': 'Прозвище',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['id', 'blocked_reason','is_blocked']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'photo']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_value']


class BooksForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(queryset=Genres.objects.all())

    class Meta:
        model = Books
        fields = ['book_name', 'book_description', 'genres', 'book_status', 'book_img', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['report_theme', 'report_content']
