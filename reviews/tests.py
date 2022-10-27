import jwt

from unittest.mock import MagicMock, patch
from django.test   import TestCase, Client
from reviews.models import ColorCode, Review

from users.models import SocialPlatform, User, Group
from my_settings  import SECRET_KEY, ALGORITHM

class MockMovieResponse:
    def json():
        json = {
            "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
            "adult": False,
            "belongs_to_collection": None,
            "budget": 63000000,
            "genres": [
                {
                "id": 18,
                "name": "Drama"
                }
            ],
            "homepage": "",
            "id": 550,
            "imdb_id": "tt0137523",
            "original_language": "en",
            "original_title": "Fight Club",
            "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
            "popularity": 0.5,
            "poster_path": None,
            "production_companies": [
                {
                "id": 508,
                "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
                "name": "Regency Enterprises",
                "origin_country": "US"
                },
                {
                "id": 711,
                "logo_path": None,
                "name": "Fox 2000 Pictures",
                "origin_country": ""
                },
                {
                "id": 20555,
                "logo_path": None,
                "name": "Taurus Film",
                "origin_country": ""
                },
                {
                "id": 54050,
                "logo_path": None,
                "name": "Linson Films",
                "origin_country": ""
                },
                {
                "id": 54051,
                "logo_path": None,
                "name": "Atman Entertainment",
                "origin_country": ""
                },
                {
                "id": 54052,
                "logo_path": None,
                "name": "Knickerbocker Films",
                "origin_country": ""
                },
                {
                "id": 25,
                "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
                "name": "20th Century Fox",
                "origin_country": "US"
                }
            ],
            "production_countries": [
                {
                "iso_3166_1": "US",
                "name": "United States of America"
                }
            ],
            "release_date": "1999-10-12",
            "revenue": 100853753,
            "runtime": 139,
            "spoken_languages": [
                {
                "iso_639_1": "en",
                "name": "English"
                }
            ],
            "status": "Released",
            "tagline": "How much can you know about yourself if you've never been in a fight?",
            "title": "Fight Club",
            "video": False,
            "vote_average": 7.8,
            "vote_count": 3439
        }
        return json

class MockS3UploadImageUrl:
    text = 'https://mblogthumb-phinf.pstatic.net/MjAxOTEwMTFfNjEg/MDAxNTcwNzg1ODM3Nzc0.zxDXm20VlPdQv8GQi9LWOdPwkqoBdiEmf8aBTWTsPF8g.FqMQTiF6ufydkQxrLBgET3kNYAyyKGJTWTyi1qd1-_Ag.PNG.kkson50/sample_images_01.png?type=w800'

class ReviewTest(TestCase):
    mixDiff = None
    
    @classmethod
    def setUpTestData(cls):
        group = Group.objects.create(
            name = 'user'
        )
        
        social_platform = SocialPlatform.objects.create(
            name = 'naver'
        )
        
        cls.user = User.objects.create(
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
        
        Review.objects.create(
            title = 'testReview',
            content = 'testReviewContents',
            rating  = 5.0,
            watched_date = '2022-10-26',
            watched_time = '19:43:14',
            user = cls.user,
            movie_id = 550
        )
        
        cls.token  = jwt.encode({'id':User.objects.get(id=1).id}, SECRET_KEY, algorithm=ALGORITHM)
        cls.header = {'HTTP_Authorization': cls.token}
        cls.payload = jwt.decode(cls.token, SECRET_KEY, algorithms=ALGORITHM)

        cls.color_code = [
            ColorCode(id=1,  color_code='#af4448'),
            ColorCode(id=2,  color_code='#ba2d65'),
            ColorCode(id=3,  color_code='#883997'),
            ColorCode(id=4,  color_code='#65499c'),
            ColorCode(id=5,  color_code='#49599a'),
            ColorCode(id=6,  color_code='#2286c3'),
            ColorCode(id=7,  color_code='#0093c4'),
            ColorCode(id=8,  color_code='#009faf'),
            ColorCode(id=9,  color_code='#00867d'),
            ColorCode(id=10, color_code='#519657'),
            ColorCode(id=11, color_code='#7da453'),
            ColorCode(id=12, color_code='#c88719'),
            ColorCode(id=13, color_code='#c75b39'),
            ColorCode(id=14, color_code='#725b53'),
            ColorCode(id=15, color_code='#aeaeae'),
            ColorCode(id=16, color_code='#62757f'),
        ]
        
        cls.color_code = ColorCode.objects.bulk_create(cls.color_code)
    
    client = Client()
      
    @patch('reviews.views.requests.get', return_value=MockMovieResponse)
    def test_review_get_success(self, mocked_requests):
        mocked_requests.get = MagicMock()
        
        response = self.client.get("/review/movie/550", **self.header)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message': 'SUCCESS', 
            'result' : {
                'review_id'    : 1,
                'title'        : 'testReview',
                'content'      : 'testReviewContents',
                'rating'       : '5.0',
                'with_user'    : '',
                'watched_date' : '2022-10-26 19:43:14',
                'review_images': [],
                'place'        : [],
                'tags'         : [],
                'movie'        : {
                    'id'      : 550,
                    'title'   : 'Fight Club',
                    'country' : 'United States of America',
                    'category': 'movie'
                    }
                }
            }
        )

    @patch('core.storages.MyS3Client.upload', return_value=MockS3UploadImageUrl)
    def test_review_post_success(self, mocked_response):
        data = {
            'user'          : self.user,
            'movie_id'      : 551,
            'title'         : 'title',
            'content'       : 'content',
            'rating'        : 4.3,
            'watched_date'  : '2022-10-26 19:43:14',
            'with_user'     : 'with_user',
            'review_images' : ['file1', 'file2'],
            'place_info'    : [124.03, 123.23, 'place_name', 'link'],
            'tags'          : ['aaaa', 'bbbb', 'cccc']
        }
        
        response = self.client.post('/review', data=data, **self.header)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': 'SUCCESS'})