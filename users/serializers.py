from rest_framework import serializers
from .models        import User, ProfileImage
from movies.models  import Image

class KakaoLoginSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.StringRelatedField()
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email', 'profile_image_url']