from django.db import models

from core.models import TimeStampedModel

class ColorCode(models.Model):
    color_code = models.CharField(max_length=50)

    class Meta:
        db_table = 'color_codes'

class Tag(models.Model):
    name       = models.CharField(max_length=50)
    color_code = models.ForeignKey('ColorCode', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tags'

class Review(TimeStampedModel):
    title         = models.CharField(max_length=100)
    content       = models.TextField(max_length=1000)
    rating        = models.DecimalField(max_digits=2, decimal_places=1)
    watched_date  = models.DateField(auto_now=False, auto_now_add=False)
    watched_time  = models.TimeField(auto_now=False, auto_now_add=False)
    watched_place = models.CharField(max_length=100)
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE)
    movie         = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    tag           = models.ForeignKey('Tag', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'reviews'

class ImageReview(models.Model):
    image  = models.ForeignKey('movies.Image', on_delete=models.CASCADE)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)    
    
    class Meta:
        db_table = 'image_reviews'
