import requests, jwt, datetime

from django.shortcuts        import redirect
from django.views            import View
from django.http             import JsonResponse
from rest_framework.views    import APIView
from rest_framework.response import Response

from my_settings       import SECRET_KEY, ALGORITHM, KAKAO_REST_API_KEY, NAVER_CLIENT_ID, NAVER_CLIENT_SECRET
from users.models      import User, SocialPlatform, Group, ProfileImage
from movies.models     import Image
from users.serializers import KakaoLoginSerializer
from core.utils        import login_decorator

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
        refresh_token  = token_response.json().get('refresh_token')
        user_info      = requests.get(
            'https://kapi.kakao.com/v2/user/me',
            headers={'Authorization': f'Bearer ${access_token}'}
            ).json()
        
        kakao_url      = 'https://kapi.kakao.com/v2/user/me'
        headers        = {'Authorization': f'Bearer {access_token}'}
        kakao_response = requests.get(kakao_url, headers = headers, timeout = 5).json()
        
        social_id      = kakao_response['id']
        nickname       = kakao_response['kakao_account']['profile']['nickname']
        profile_image  = kakao_response['kakao_account']['profile']['profile_image_url']
        email          = kakao_response['kakao_account']['email']
    
        #* 기존 가입한 유저가 로그인 할 때
        if User.objects.filter(social_id=social_id).exists():
            user_info     = User.objects.get(social_id=social_id)
            access_token  = jwt.encode({'id': user_info.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
            refresh_token = jwt.encode({'id': user_info.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)
        
            User.objects.filter(id=user_info.id).update(
                refresh_token = refresh_token
            )
        
            token_info = {
                'access_token' : access_token,
                'refresh_token': refresh_token
                }
            
            data = {
                'social_id'     : social_id,
                'nickname'      : nickname,
                'email'         : email,
                'profile_image' : profile_image,
            }
        
            return Response({'user_info': data, 'token_info': token_info}, status=201)
        
        else:
            #* 신규 유저가 로그인 할 때 (회원가입)
            user = User.objects.create(
                social_id          = social_id,
                nickname           = nickname,
                social_platform_id = SocialPlatform.objects.get(name="kakao").id,
                email              = email,
                group_id           = Group.objects.get(id=2).id,
            )
            
            image = Image.objects.create(
                image_url = profile_image
            )
            
            ProfileImage.objects.create(
                user  = user,
                image = image
            )
            
            access_token  = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
            refresh_token = jwt.encode({'id': social_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)
            
            token_info = {
                'access_token' : access_token,
                'refresh_token': refresh_token
                }
            
            data = {
                'social_id'     : social_id,
                'nickname'      : nickname,
                'email'         : email,
                'profile_image' : profile_image
            }
            
            return Response({'user_info': data, 'token_info': token_info}, status=201)

        
        # except User.DoesNotExist:
        #     return JsonResponse({'message': 'INVALID_USER'}, status=404)
        
        # except KeyError:
        #     return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        
        
class DeleteAccountView(APIView):
    @login_decorator
    def delete(self, request):
        user = request.user
        user.delete()
        
        return Response({'message': 'DELETE_SUCCESS'}, status=204)

#NaverLogin
# TODO : DRF 적용
class LoginNaverView(View):
    def get(self, request):
        try:
            naver_access_token  = request.GET.get('access_token')
            naver_refresh_token = request.GET.get('refresh_token')
            headers             = {'Authorization' : 'Bearer '+ naver_access_token}
            profile_api_url     = "https://openapi.naver.com/v1/nid/me"
            
            user_info_dict      = requests.get(profile_api_url, headers=headers, timeout=5).json()
            user_info           = user_info_dict['response']

            if(user_info_dict['message']!= 'success'):
                return JsonResponse({'message' : user_info_dict['message'], 'ressultcode': user_info_dict['resultcode']}, status=400)
            
            user = User.objects.filter(social_id=user_info['id'])
            
            if(user.exists()):
                user = User.objects.get(social_id=user_info['id'])
                #user.refresh_token = naver_refresh_token
                #user.save()
                
            else:
                user = User.objects.create(
                    social_id       = user_info['id'],
                    nickname        = user_info['name'],
                    email           = user_info['email'],
                    group           = Group.objects.get(name='general'),
                    #refresh_token   = naver_refresh_token,
                    social_platform = SocialPlatform.objects.get(name='naver')
                )
                
                # TODO : S3업로더 생성 후 S3업로드하고, image_url 반영
                default_image_url = 'https://cdn.pixabay.com/photo/2018/11/13/21/43/avatar-3814049_1280.png'
            
                user_image = Image.objects.create(image_url=user_info['profile_image', default_image_url])
                ProfileImage.objects.create(user=user, image=user_image)
            
            access_token = jwt.encode({'id':user.id, 
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
            
            refresh_token = jwt.encode({'id':user.id, 
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)
            
            user.refresh_token = refresh_token
            user.save()
            
            token_info = {
                'access_token':access_token,
                'refresh_token':refresh_token 
            }
            
            return JsonResponse({
                'message':'SUCCESS',
                'token_info': token_info
                }, status=200)        

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)         

class LoginNaverCallBackView(View):
    def get(self, request):
        token_api_uri = 'https://nid.naver.com/oauth2.0/token'
        data = {
            'grant_type'    :'authorization_code',
            'client_id'     : NAVER_CLIENT_ID,
            'client_secret' : NAVER_CLIENT_SECRET,
            'code'          : request.GET.get('code'),
            # TODO : state세션에 저장 후, 로그인 요청시 검증할 수 있도록 할 것
            'state'         : 'state',
        }
        
        token_response = requests.post(token_api_uri, data=data)
        token_info     = token_response.json()
        
        access_token  = token_info['access_token']
        refresh_token = token_info['refresh_token']
        token_type    = token_info['token_type']
        expires_in    = token_info['expires_in']
        
        return redirect(f'http://localhost:8000/users/login/naver?access_token={access_token}&refresh_token={refresh_token}&token_type={token_type}&expires_in={expires_in}')

class UserInformationView(View):
    @login_decorator
    def get(self, request):
        try:
            user          = request.user
            profile_image = ProfileImage.objects.get(user_id=user.id).image.image_url
            result = {
                'nickname'      : user.nickname,
                'email'         : user.email,
                'Profile_image' : profile_image
            }
            return JsonResponse({'message': 'SUCCESS', 'result' : result}, status=200)
    
        except KeyError:
            return JsonResponse({'message': 'KEYERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)