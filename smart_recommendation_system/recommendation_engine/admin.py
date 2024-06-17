from django.contrib import admin
from .models import Genre, Movie, Series, Song, SongsLanguage

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(Song)
admin.site.register(SongsLanguage)

