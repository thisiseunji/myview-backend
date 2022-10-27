import jwt

from unittest.mock import MagicMock, patch
from django.test   import TestCase, Client
from reviews.models import Review

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

@patch('reviews.views.requests.get', return_value=MockMovieResponse)
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

    client = Client()

    def test_review_get_success(self, mocked_requests):
        
        mocked_requests.get = MagicMock()
        
        response = self.client.get("/review/movie/550", **self.header)
        
        result = response
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result.json(), {
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