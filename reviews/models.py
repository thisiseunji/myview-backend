from django.db import models

from core.models import TimeStampedModel

class ColorCode(models.Model):
    color_code = models.CharField(max_length=50)

    class Meta:
        db_table = 'color_codes'

class Tag(models.Model):
    name       = models.CharField(max_length=50)

    class Meta:
        db_table = 'tags'

class Review(TimeStampedModel):
    title         = models.CharField(max_length=100)
    content       = models.TextField(max_length=1000)
    rating        = models.DecimalField(max_digits=2, decimal_places=1)
    watched_date  = models.DateField(auto_now=False, auto_now_add=False)
    watched_time  = models.TimeField(auto_now=False, auto_now_add=False)
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE)
    movie         = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reviews'
        
class ReviewTag(models.Model):
    Review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE)
    Tag    = models.ForeignKey('reviews.Tag', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reviewtags'

class Place(models.Model):
    name = models.CharField(max_length=50)
    mapx = models.FloatField(max_length=100)
    mapy = models.FloatField(max_length=100)
    link = models.URLField(max_length=500)

    class Meta:
        db_table = 'places'
        
class ReviewPlace(TimeStampedModel):
    review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE)
    place  = models.ForeignKey('reviews.Place', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_places'

class ImageReview(models.Model):
    image  = models.ForeignKey('movies.Image', on_delete=models.CASCADE)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'image_reviews'
        
        
class ReviewUser(TimeStampedModel):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)    
    user   = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'review_users'
