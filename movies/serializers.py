from rest_framework import serializers
from .models        import Movie, ThumbnailImage, MovieImage


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'country', 'category']