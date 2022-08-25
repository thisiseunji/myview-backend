from django.db import models

from core.models import TimeStampedModel

class ColorCode(models.Model):
    color_code = models.CharField(max_length=50)

    class Meta:
        db_table = 'color_codes'

class Tag(models.Model):
    name       = models.CharField(max_length=50)
    color_code = models.ForeignKey('reviews.ColorCode', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tags'

class Review(TimeStampedModel):
    title         = models.CharField(max_length=100, blank=True)
    content       = models.TextField(max_length=1000, blank=True)
    rating        = models.DecimalField(max_digits=2, decimal_places=1)
    watched_date  = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    watched_time  = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    with_user     = models.CharField(max_length=30, blank=True)
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE)
    movie_id      = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'reviews'
        
class ReviewTag(models.Model):
    review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE)
    tag    = models.ForeignKey('reviews.Tag', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'review_tags'

class Place(models.Model):
    name = models.CharField(max_length=50, blank=True)
    mapx = models.FloatField(max_length=100, blank=True, null=True)
    mapy = models.FloatField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=500, blank=True)

    class Meta:
        db_table = 'places'
        
class ReviewPlace(TimeStampedModel):
    review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE)
    place  = models.ForeignKey('reviews.Place', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_places'

class ReviewImage(models.Model):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)    
    image  = models.ForeignKey('adminpage.Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'review_images'
        
class ReviewUser(TimeStampedModel):
    review = models.ForeignKey('Review', on_delete=models.CASCADE)    
    user   = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'review_users'