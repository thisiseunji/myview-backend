import requests, jwt, datetime

from django.shortcuts        import redirect
from django.views            import View
from django.http             import JsonResponse
from rest_framework.views    import APIView
from rest_framework.response import Response

from my_settings       import SECRET_KEY, ALGORITHM, KAKAO_REST_API_KEY
from users.models      import User, SocialPlatform, Group
from users.serializers import KakaoLoginSerializer


class KakaoLogInView(APIView):
    def get(self, request):
        try:
            kakao_token    = request.headers.get('Authorization', None)
            kakao_url      = 'https://kapi.kakao.com/v2/user/me'
            headers        = {'Authorization': f'Bearer {kakao_token}'}
            kakao_response = requests.get(kakao_url, headers = headers, timeout = 5).json()
            
            social_id = kakao_response['id']
            nickname  = kakao_response['kakao_account']['profile']['nickname']
            email     = kakao_response['kakao_account']['email']
            
            #* 기존 가입한 유저가 로그인 할 때
            if User.objects.filter(social_id=social_id).exists():
                user_info     = User.objects.get(social_id=social_id)
                access_token  = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
                refresh_token = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)
            
                User.objects.filter(id=user_info.id).update(
                    refresh_token = refresh_token
                )
            
                token_info = {
                    'access_token' : access_token,
                    'refresh_token': refresh_token
                    }
                
                data = {
                    'social_id': social_id,
                    'nickname': nickname,
                    'email': email,
                }
            
                return Response({'user_info': KakaoLoginSerializer(instance=data).data, 'token_info': token_info}, status=201)
            
            else:
                #* 신규 유저가 로그인 할 때 (회원가입)
                User.objects.create(
                    social_id          = social_id,
                    nickname           = nickname,
                    social_platform_id = SocialPlatform.objects.get(name="kakao").id,
                    email              = email,
                    group_id           = Group.objects.get(id=2).id,
                )
                
                access_token  = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
                refresh_token = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)
                
                token_info = {
                    'access_token' : access_token,
                    'refresh_token': refresh_token
                    }
                
                data = {
                    'social_id': social_id,
                    'nickname': nickname,
                    'email': email,
                }
                
                return Response({'user_info': KakaoLoginSerializer(instance=data).data, 'token_info': token_info}, status=201)
        
        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=404)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


#* 카카오로그인 할 때
class KakaoLogIn(APIView):
    def get(self, request):
        app_key        = KAKAO_REST_API_KEY
        redirect_uri   = 'http://localhost:8000/users/login/kakao/callba'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        
        return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}')


class DeleteAccountView(APIView):
    def delete(self, request):
        # user = request.user
        user = User.objects.get(id=3)
        
        user.delete()
        
        return Response({'message': 'DELETE_SUCCESS'}, status=204)


#* 카카오 신규유저 테스트
class KakaoLogIn(APIView):
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
        access_token   = token_response.json().get('access_token')
        user_info      = requests.get(
            'https://kapi.kakao.com/v2/user/me',
            headers={'Authorization': f'Bearer ${access_token}'}
            ).json()
        
        return JsonResponse({'user_info': user_info, 'token': access_token})