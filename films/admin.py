from django.contrib import admin

# Register your models here.
from films.models import Author, Genre , Film, Favori

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Film)
admin.site.register(Favori)