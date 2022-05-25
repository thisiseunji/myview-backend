from rest_framework import serializers
from .models        import User

class KakaoLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['social_id', 'nickname', 'email']