from django.shortcuts import render
from .models import Genre, Movie, SongsLanguage, Song, Series


def home_page(request):
    return render(request, 'home.html')

def movie_page(request):
    selected_genre = request.GET.get('genre')
    if selected_genre:
        movies = Movie.objects.filter(genre__name=selected_genre)
        # movies.append(Movie.objects.all)
    else:
        movies = Movie.objects.all()
    genres = Genre.objects.all()
    return render(request, 'movie_page.html', {'movies': movies, 'genres': genres, 'selected_genre': selected_genre})
    # return render(request, 'movie_page.html')

def song_page(request):
    selected_language = request.GET.get('language')
    if selected_language:
        songs = Song.objects.filter(language__name=selected_language)
        # movies.append(Movie.objects.all)
    else:
        songs = Song.objects.all()
    languages = SongsLanguage.objects.all()
    return render(request, 'song_page.html',{'songs': songs, 'languages': languages, 'selected_language': selected_language})

def series_page(request):
    selected_genre = request.GET.get('genre')
    if selected_genre:
        series = Series.objects.filter(genre__name=selected_genre)
    else:
        series = Series.objects.all() 
    genres = Genre.objects.all()
    return render(request, 'series_page.html',{'series': series, 'genres': genres, 'selected_genre': selected_genre})