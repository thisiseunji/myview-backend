from rest_framework import serializers
from .models        import Movie


class MovieSerializer(serializers.ModelSerializer):
    ratings             = serializers.StringRelatedField()
    country             = serializers.StringRelatedField()
    category            = serializers.StringRelatedField()
    genre               = serializers.ReadOnlyField()
    actor               = serializers.ReadOnlyField()
    thumbnail_image_url = serializers.ReadOnlyField()
    image_url           = serializers.ReadOnlyField()
    video_url           = serializers.ReadOnlyField()
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'en_title', 'description', 'running_time', 'age', 'ratings', 'release_date', 'country', 'category', 'genre', 'actor', 'thumbnail_image_url', 'image_url', 'video_url']