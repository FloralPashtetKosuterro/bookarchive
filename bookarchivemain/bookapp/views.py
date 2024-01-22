from django.shortcuts import render
from bookapp.models import *
# Create your views here.

def main(request):
    getitems = Categories.objects.all()
    getnews = News.objects.all()
    data = {
        'categoryshow': getitems,
        'news': getnews,
    }
    return render(request, 'bookapp/index.html', data)