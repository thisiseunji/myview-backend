from rest_framework import serializers
from .models        import Movie, ThumbnailImage, MovieImage, Actor


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'country', 'category']
        
        
class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'