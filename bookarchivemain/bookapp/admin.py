from django.contrib import admin
from bookapp.models import *
# Register your models here.
admin.site.register(Books)
admin.site.register(Parts)
admin.site.register(Genres)
