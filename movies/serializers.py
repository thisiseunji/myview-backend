from rest_framework import serializers
from .models        import Movie, ThumbnailImage, MovieImage


class MovieSerializer(serializers.ModelSerializer):

    movie_images = serializers.StringRelatedField(many=True)
    thumbnail_images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date']