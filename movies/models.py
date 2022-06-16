from django.db import models

from core.models import TimeStampedModel

class Country(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'countries'
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'categories'

class Platform(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'platforms'
        
class Movie(TimeStampedModel):
    title        = models.CharField(max_length=200)
    description  = models.TextField(max_length=1000)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    country      = models.ForeignKey('Country', on_delete=models.CASCADE)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'movies'
        
class MoviePlatform(models.Model):
    movie    = models.ForeignKey('Movie', on_delete=models.CASCADE)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'movie_platforms'
            
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'genres'

class MovieGenre(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)   
    
    class Meta:
        db_table = 'movie_genres'

class Actor(models.Model):
    name    = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    image   = models.ForeignKey('Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'actors'

class Role(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'roles'

class MovieActor(TimeStampedModel):
    movie     = models.ForeignKey('Movie', on_delete=models.CASCADE)
    actor     = models.ForeignKey('Actor', on_delete=models.CASCADE)
    role      = models.ForeignKey('Role', on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'movie_actors'
        
class Video(models.Model):
    video_url = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'videos'

class MovieVideo(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'movie_videos'

class Image(TimeStampedModel):
    image_url = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'images'
    
class MovieImage(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'movie_images'

class ThumbnailImage(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'thumbnail_images'