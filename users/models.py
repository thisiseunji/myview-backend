from django.db    import models

from core.models    import TimeStampedModel

class Group(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'groups'
    
class SocialPlatform(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'social_platforms'
        
class User(TimeStampedModel):
    social_id       = models.CharField(max_length=200, unique=True)
    nickname        = models.CharField(max_length=50, null=True)
    email           = models.EmailField(max_length=100, null=True)
    password        = models.CharField(max_length=200, null=True)
    phone_number    = models.CharField(max_length=50, null=True)
    group           = models.ForeignKey('Group', on_delete=models.CASCADE)
    refresh_token   = models.CharField(max_length=300, null=True)
    social_platform = models.ForeignKey('SocialPlatform', on_delete=models.CASCADE)
    is_valid        = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'users'


class SocialToken(TimeStampedModel):
    access_token  = models.CharField(max_length=300, null=True)
    refresh_token = models.CharField(max_length=300, null=True)
    token_type    = models.CharField(max_length=300, null=True)
    expires_in    = models.CharField(max_length=300, null=True)
    
    class Meta:
        db_table = 'social_tokens'
        
class ProfileImage(TimeStampedModel):
    user  = models.ForeignKey('User', on_delete=models.CASCADE)
    image = models.ForeignKey('adminpage.Image', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'profile_images'

class Collection(TimeStampedModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'collections'

class CollectionMovie(models.Model):
    movie_id   = models.CharField(max_length=1000)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'collection_movies'