import requests, jwt, datetime, random

from django.shortcuts        import redirect
from django.views            import View
from django.http             import JsonResponse
from rest_framework.views    import APIView
from rest_framework.response import Response


from users.models     import User, SocialPlatform, Group, ProfileImage, SocialToken
from reviews.models   import Review
from adminpage.models import Image
from core.utils       import login_decorator
from core.tmdb        import tmdb_helper
from my_settings      import AWS_S3_URL, SECRET_KEY, ALGORITHM, KAKAO_REST_API_KEY, NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, TMDB_IMAGE_BASE_URL


#* 카카오 신규유저 테스트
class KakaoLogIn(APIView):
    def get(self, request):
        app_key        = KAKAO_REST_API_KEY
        redirect_uri   = 'http://localhost:8000/user/login/kakao/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'
        
        return redirect(f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}')

class KakaoLogInCallbackView(APIView):
    def get(self, request):
        try:
            auth_code       = request.GET.get('code')
            kakao_token_api = 'https://kauth.kakao.com/oauth/token'
            data            = {
                'grant_type'      : 'authorization_code',
                'client_id'       : KAKAO_REST_API_KEY,
                'redirection_uri' : 'https://kauth.kakao.com/oauth/authorize?response_type=code',
                'code'            : auth_code
            }

            token_response = requests.post(kakao_token_api, data=data)
            social_access_token   = token_response.json().get('access_token')
            social_refresh_token  = token_response.json().get('refresh_token')
            token_type  = token_response.json().get('token_type')
            expires_in  = token_response.json().get('refresh_token_expires_in')
            
            user_info      = requests.get(
                'https://kapi.kakao.com/v2/user/me',
                headers={'Authorization': f'Bearer ${social_access_token}'}
                ).json()

            kakao_url      = 'https://kapi.kakao.com/v2/user/me'
            headers        = {'Authorization': f'Bearer {social_access_token}'}
            kakao_response = requests.get(kakao_url, headers = headers, timeout = 5).json()

            social_id         = kakao_response['id']
            nickname          = kakao_response['kakao_account']['profile']['nickname']
            profile_image_url = kakao_response['kakao_account']['profile']['profile_image_url']
            
            SocialToken.objects.update_or_create(
                    refresh_token = social_refresh_token,
                    defaults={
                        'access_token'  : social_access_token,
                        'refresh_token' : social_refresh_token,
                        'token_type'    : token_type,
                        'expires_in'    : expires_in,
                    }
                )
            
            #* 기존 가입한 유저가 로그인 할 때
            if User.objects.filter(social_id=social_id).exists():
                user          = User.objects.get(social_id=social_id)
                access_token  = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
                refresh_token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)

                User.objects.filter(id=user.id).update(
                    refresh_token = refresh_token,
                )
                
                token_info = {
                    'access_token' : access_token,
                    'refresh_token': refresh_token
                    }
                
                return Response({'token_info': token_info}, status=201)

            #* 신규 유저가 로그인 할 때 (회원가입) 
            else:
                user = User.objects.create(
                    social_id       = social_id,
                    nickname        = nickname,
                    social_platform = SocialPlatform.objects.get(name='kakao'),
                    group_id        = Group.objects.get(id=2).id,
                )
                
                image = Image.objects.create(
                    image_url = profile_image_url
                )

                ProfileImage.objects.create(
                    user  = user,
                    image = image
                )
                
                access_token  = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=6)}, SECRET_KEY, ALGORITHM)
                refresh_token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY, ALGORITHM)

                user.refresh_token=refresh_token
                user.save()
                
                token_info = {
                    'access_token' : access_token,
                    'refresh_token': refresh_token
                    }
                
                return Response({'token_info': token_info}, status=201)
        
        except User.DoesNotExist:
            return Response({'message': 'INVALID_USER'}, status=400)
        
        except KeyError:
            return Response({'message': 'KEY_ERROR'}, status=400)
        
#NaverLogin
class LoginNaverCallBackView(View):
    def get(self, request):
        token_api_uri = 'https://nid.naver.com/oauth2.0/token'
        data = {
            'grant_type'    : 'authorization_code',
            'client_id'     : NAVER_CLIENT_ID,
            'client_secret' : NAVER_CLIENT_SECRET,
            'code'          : request.GET.get('code'),
            # TODO : state세션에 저장 후, 로그인 요청시 검증할 수 있도록 할 것
            'state'         : 'state',
        }
        
        token_response = requests.post(token_api_uri, data=data)

        token_info    = token_response.json()
        access_token  = token_info['access_token']
        refresh_token = token_info['refresh_token']
        token_type    = token_info['token_type']
        expires_in    = token_info['expires_in']

        user_info = requests.get('https://openapi.naver.com/v1/nid/me', headers={'Authorization':'Bearer '+ access_token}, timeout=5).json()

        if(user_info['message']!= 'success'):
            return JsonResponse({'message' : user_info['message'], 'ressultcode': user_info['resultcode']}, status=400)
        
        user = User.objects.filter(social_id=user_info['response']['id'])

        if user.exists():
            user = User.objects.get(social_id=user_info['response']['id'])
            
        else:
            user = User.objects.create(
                social_id       = user_info['response']['id'],
                nickname        = user_info['response']['name'],
                email           = user_info['response'].get('email', None),
                group           = Group.objects.get(id=2),
                social_platform = SocialPlatform.objects.get(id=3)
            )
            
            user_image    = Image.objects.create(image_url=user_info['response']['profile_image'])
            profile_image = ProfileImage.objects.create(user_id=user.id, image_id=user_image.id)
            
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
            'message'   : 'SUCCESS',
            'token_info': token_info,
            }, status=200)        
     
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
        
class UserProfileUpdateView(APIView):
    @login_decorator
    def patch(self, request):
        try:
            data         = request.GET
            user         = request.user
            nickname     = data.get('nickname')
            email        = data.get('email')
            phone_number = data.get('phone_number')
            
            if nickname:
                user.nickname = nickname
            if email:
                user.email = email
            if phone_number:
                user.phone_number = phone_number
            
            user.save()
                
            return Response({'message': 'PROFILE_UPDATE_SUCCESS'}, status=201)
        
        except User.DoesNotExist:
            return Response({'message': 'USER_NOT_EXIST'}, status=400)
        
        except KeyError:
            return Response({'message': 'KEY_ERROR'}, status=400)
        
class DeleteAccountView(APIView):
    @login_decorator
    def delete(self, request):
        try:
            user = request.user
            user.is_valid = False
            user.save()
            
            return Response({'message': 'DELETE_SUCCESS'}, status=204)
        
        except User.DoesNotExist:
            return Response({'message': 'USER_NOT_EXIST'}, status=400)
        

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        
        user_data = [{
            'id'                : user.id,
            'social_platform'   : user.social_platform.name,
            'social_id'         : user.social_id,
            'nickname'          : user.nickname,
            'email'             : user.email,
            'phone_number'      : user.phone_number,
            'group'             : user.group.name,
            'is_valid'          : user.is_valid,
            'review_count'      : len(Review.objects.filter(user_id=user.id)),
            'profile_image_url' : AWS_S3_URL+ProfileImage.objects.get(user_id=user.id).image.image_url,
            } for user in users]
        
        return Response({'data': user_data}, status=200)
    
# class LoginBackGroundView(APIView):
#     def get(self, request):
#         image_length = len(MovieImage.objects.all())
#         movie_image  = MovieImage.objects.get(id=randrange(1, image_length+1))
        
#         data = {
#             'movie_id'    : movie_image.movie.id,
#             'title'       : movie_image.movie.title,
#             'description' : movie_image.movie.description,
#             'image_url'   : AWS_S3_URL+movie_image.image.image_url
#         }
        
#         return JsonResponse({'data': data}, status=200)

#tmdb
class LoginBackGroundView(APIView):
    def get(self, request):
        random_num             = random.randrange(1,100)
        
        image_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(random_num)+'/images')
        image_data_raw_data    = requests.get(image_data_request_url)
        image_data             = image_data_raw_data.json()
        
        while image_data.get('backdrops') == None or image_data.get('backdrops') == []:
            random_num             += 101
            image_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(random_num)+'/images')
            image_data_raw_data    = requests.get(image_data_request_url)
            image_data             = image_data_raw_data.json()
        
        movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(random_num), region='KR', language='ko')
        movie_data_raw_data    = requests.get(movie_data_request_url)
        movie_data             = movie_data_raw_data.json()
        
        data = {
            'movie_id'    : random_num,
            'title'       : movie_data.get('title'),
            'description' : movie_data.get('overview'),
            'image_url'   : TMDB_IMAGE_BASE_URL+image_data.get('backdrops')[0].get('file_path'),
        }
        
        return JsonResponse({'data': data}, status=200)