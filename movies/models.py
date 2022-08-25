from django.db import models

class Platform(models.Model):
    name      = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    url       = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'platforms'