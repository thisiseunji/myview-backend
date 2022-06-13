from rest_framework import serializers
from .models        import User, ProfileImage
from movies.models  import Image


class KakaoLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'nickname', 'email']