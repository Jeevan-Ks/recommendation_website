from django.conf import settings
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    director = models.TextField(default="")
    stars = models.TextField(default="")
    image = models.ImageField(default="")
    
    def __str__(self):
        return self.title
    
class SongsLanguage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    language = models.ForeignKey(SongsLanguage, on_delete=models.CASCADE)
    singer = models.TextField()
    music = models.TextField()
    image = models.ImageField(default="")
    
    def __str__(self):
        return self.title
    
class Series(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField()
    director = models.TextField()
    cast = models.TextField()
    seasons = models.TextField()
    image = models.ImageField(upload_to='')
    
    def __str__(self):
        return self.title