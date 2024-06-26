from django.contrib import admin
from bookapp.models import *
from django.contrib.auth.admin import UserAdmin

admin.site.register(Books)
admin.site.register(Parts)
admin.site.register(Genres)
admin.site.register(Comments)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Rating)
admin.site.register(Reports)
