from django.db import models

from core.models import TimeStampedModel

class Image(TimeStampedModel):
    image_url = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'images'