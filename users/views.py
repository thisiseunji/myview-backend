import requests, jwt, datetime

from django.shortcuts     import redirect
from django.views         import View
from django.http          import JsonResponse
from rest_framework.views import APIView

from users.models import User
from my_settings  import SECRET_KEY, ALGORITHM, KAKAO_REST_API_KEY


class KakaoLogInView(APIView):
    def get(self, request):
        app_key        = KAKAO_REST_API_KEY
        redirect_uri   = 'http://localhost:8000/users/login/kakao/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        
        return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}')

class KakaoLogInCallbackView(APIView):
    def get(self, request):
        auth_code       = request.GET.get('code')
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data            = {
            'grant_type'      : 'authorization_code',
            'client_id'       : KAKAO_REST_API_KEY,
            'redirection_uri' : 'https://kauth.kakao.com/oauth/authorize?response_type=code',
            'code'            : auth_code
        }
        
        token_response = requests.post(kakao_token_api, data=data)
        
        access_token = token_response.json().get('access_token')
        
        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization': f'Bearer ${access_token}'})
        
        return JsonResponse({'user_info': user_info_response.json()})