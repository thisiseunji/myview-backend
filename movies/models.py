from django.db import models

class CountryCode(models.Model):
    iso_code = models.CharField(max_length=20)
    name     = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'country_codes'
        
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'genres'
