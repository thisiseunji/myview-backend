import jwt

from rest_framework.test import APITestCase, APIClient
from django.test         import TestCase, Client
from unittest.mock       import MagicMock, patch

from users.models     import ProfileImage, SocialPlatform, User, Group
from adminpage.models import Image
from my_settings      import SECRET_KEY, ALGORITHM 

class MockNaverTokenDataResponse:
    def json():
        token_info = {
            'access_token' : 'naver_access_token',
            'refresh_token' : 'naver_refresh_token',
            'token_type' : 'naver_token_type',
            'expires_in' : 'expires_in'
        }
        return token_info

class MockNaverUserDataResponse:
    def json():
        user_info = {
            'message' : 'success',
            'response' : {
                'id' : 'social_id',
                'name' : 'social_name',
                'email' : 'pony@naver.com',
                'profile_image' : 'profile_image'
            }
        }
        return user_info

class LoginTest(APITestCase):
    maxDiff = None
    
    @classmethod
    def setUpTestData(cls):
        group = Group.objects.create(
            id = 2,
            name = 'user'
        )
        
        social_platform = SocialPlatform.objects.create(
            id = 3,
            name = 'naver'
        )

    client = Client()
    
    @patch('users.views.requests.post', MagicMock(return_value=MockNaverTokenDataResponse))
    @patch('users.views.requests.get', MagicMock(return_value=MockNaverUserDataResponse))    
    def test_naver_login_test(self):
        
        response = self.client.get('/user/login/naver/callback')

class UserInformationTest(TestCase):
    maxDiff = None
    
    @classmethod
    def setUpTestData(cls):
        group = Group.objects.create(
            name = 'user'
        )
        
        social_platform = SocialPlatform.objects.create(
            name = 'naver'
        )
        
        cls.user = User.objects.create(
            id        = 2,
            social_id = '소셜아이디',
            nickname  = '테스트유저',
            email     = 'test@naver.com',
            password  = 'password',
            phone_number = '000-0000-0000',
            group     = group,
            refresh_token = 'ref_token',
            social_platform = social_platform,
            is_valid  = True
        )

        cls.token  = jwt.encode({'id':User.objects.get(id=2).id}, SECRET_KEY, algorithm=ALGORITHM)
        cls.header = {'HTTP_Authorization': cls.token}
        cls.payload = jwt.decode(cls.token, SECRET_KEY, algorithms=ALGORITHM)
        
        cls.image = Image.objects.create(
            image_url = 'test_image_url'
        )
        
        ProfileImage.objects.create(
            user = cls.user,
            image = cls.image
        )
        
    clent = APIClient()
    
    def test_user_information_get(self):
        
        response = self.client.get('/user/info', **self.header)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message': 'SUCCESS', 
            'result': {
                        'nickname': '테스트유저', 
                        'email': 'test@naver.com', 
                        'Profile_image': 'test_image_url'
                    }
                }
        )
        
    def test_user_profile_update_patch(self):
        
        data = {'phone_number' : '111-0000-0000'}
        
        response = self.client.patch('/user/update', data=data, **self.header)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'PROFILE_UPDATE_SUCCESS'})
    
    def test_user_account_delete(self):
        
        response = self.client.delete('/user/delete', **self.header)
