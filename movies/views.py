from random import randrange
import requests, jwt

from django.http             import JsonResponse
from django.views            import View
from rest_framework.views    import APIView
from rest_framework.response import Response

from movies.models           import Genre
from reviews.models          import Review
from users.models            import ProfileImage, User
from my_settings             import AWS_S3_URL, TMDB_IMAGE_BASE_URL, TMDB_VIDEO_BASE_URL, SECRET_KEY, ALGORITHM
from core.tmdb               import tmdb_helper

basic_img = 'https://pixabay.com/ko/photos/%eb%a7%90-%ec%a2%85%eb%a7%88-%ea%b0%88%ea%b8%b0-%ed%8f%ac%ec%9c%a0-%eb%8f%99%eb%ac%bc-5625922/'

#tmdb 수정
class MovieDetailView(APIView):
    def get(self, request):
        movie_id = request.GET.get('movie_id')
        page     = int(request.GET.get('page', 0))
        limit    = int(request.GET.get('limit', 10))
        offset   = page*limit
        
        total_page = -1
        
        # MOVIES / Get Details
        movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id), region='KR', language='ko')
        movie_data_raw_data = requests.get(movie_data_request_url)
        movie_data = movie_data_raw_data.json()
        
        if movie_data.get('id') == None :
            return Response('{message : INVALID_DATA}', status=404)
        
        # MOVIES / Get credits
        actor_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id)+'/credits', language='ko')
        actor_data_raw_data = requests.get(actor_data_request_url)
        actor_data = actor_data_raw_data.json()
        
        if actor_data['cast']:
           total_page = (len(actor_data['cast'])//limit)-1 if len(actor_data['cast'])%limit == 0 else (len(actor_data['cast'])//limit)
        
        # MOVIES / Get Images
        image_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id)+'/images')
        image_data_raw_data = requests.get(image_data_request_url)
        image_data = image_data_raw_data.json()
        
        # MOVIES / Get Videos
        video_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id)+'/videos', language='ko')
        video_data_raw_data = requests.get(video_data_request_url)
        video_data = video_data_raw_data.json()
        
        # MOVIES / Get Watch Providers
        provider_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id)+'/watch/providers')
        provider_data_raw_data = requests.get(provider_data_request_url)
        provider_data = provider_data_raw_data.json()
        
        movie_data = {
            'total_page'          : total_page,
            'id'                  : movie_data.get('id'),
            'title'               : movie_data.get('title'),
            'en_title'            : movie_data.get('original_title'),
            'description'         : movie_data.get('overview'),
            'running_time'        : movie_data.get('runtime'),
            'age'                 : movie_data.get('adult'),
            'ratings'             : round(float(movie_data.get('vote_average'))/2,0),
            'release_date'        : movie_data.get('release_date'),
            'country'             : movie_data.get('production_countries')[0].get('name') if movie_data.get('production_countries') != (None or []) else '',
            'category'            : '미구현 제공여부 확인중',
            'genre'               : [{
                'name': genre.get('name'),
                'color_code' : Genre.objects.get(id=genre.get('id')).color_code,
                }for genre in movie_data.get('genres')] if movie_data.get('genres') != (None or []) else '',
            'platform_name'       : [provider.get('provider_name') for provider in provider_data.get('results').get('KR').get('buy')] if provider_data.get('results') != None and provider_data.get('results').get('KR') != None and provider_data.get('results').get('KR').get('buy') != None else '',
            'platform_logo_image' : [TMDB_IMAGE_BASE_URL+provider.get('logo_path') for provider in provider_data.get('results').get('KR').get('buy')] if provider_data.get('results') != None and provider_data.get('results').get('KR') != None and provider_data.get('results').get('KR').get('buy') != None else '',
            'actor'               : [{
                'id'        : actor.get('id'),
                'name'      : actor.get('name'),
                'image'     : TMDB_IMAGE_BASE_URL+actor.get('profile_path') if actor.get('profile_path') != None else 'basic_img',
                'role'      : actor.get('known_for_department'),
                'role_name' : actor.get('character'),
                } for actor in actor_data.get('cast')][offset:offset+limit] if actor_data.get('cast') != None else '',  
            'thumbnail_image_url' : TMDB_IMAGE_BASE_URL+movie_data.get('poster_path') if movie_data.get('poster_path') != None else '',
            'image_url'           : [TMDB_IMAGE_BASE_URL+image.get('file_path') for image in image_data.get('backdrops')][:20] if image_data.get('backdrops') != None else '',
            'video_url'           : [TMDB_VIDEO_BASE_URL+video.get('key') for video in video_data.get('results')][:4] if video_data.get('results') != None else '',
            }
        
        return Response({'movie_info': movie_data}, status=200)


class MovieReviewView(View):
    def get(self, request, movie_id):
        reviews = Review.objects.filter(movie_id=movie_id).order_by('-created_at', 'title', 'id')
        reviews = [
            {
                'review_id' : review.id,
                'name'      : review.user.nickname,
                'profile'   : AWS_S3_URL+ProfileImage.objects.get(user_id=review.user.id).image.image_url,
                'title'     : review.title,
                'content'   : review.content,
                'rating'    : review.rating,
            } for review in reviews]
        
        return JsonResponse({'message':'SUCCESS', 'result':reviews}, status=200)


#tmdb  
class MoviePopularView(APIView):
    def get(self, request):
        request_url    = tmdb_helper.get_request_url(method='/movie/popular', language='ko-KR', region='KR')
        popular_movies = requests.get(request_url).json()
        
        rank   = []
        
        for movie in popular_movies['results'][:10]:
            rank.append({
                'id'    : movie['id'],
                'title' : movie['title']
            })
            
        return JsonResponse({'message':'SUCCESS', 'rank':rank}, status=200)
    
class MovieLatestView(APIView):
    def get(self, request):
        request_url   = tmdb_helper.get_request_url(method='/movie/now_playing', language='ko-KR', region='KR')
        latest_movies = requests.get(request_url).json()
        result        = []
        
        for movie in sorted(latest_movies.get('results'), key=lambda x: x.get('popularity'), reverse=True)[:10]:
            
            movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie['id']), region='KR', language='ko-KR')
            movie_data_raw_data    = requests.get(movie_data_request_url)
            movie_data             = movie_data_raw_data.json()
            
            result.append( {
                'id'           : movie['id'],
                'title'        : movie['title'],
                'poster'       : TMDB_IMAGE_BASE_URL + movie['poster_path'],
                'release_date' : movie['release_date'],
                'ratings'      : movie['vote_average'],
                'country'      : movie_data.get('production_countries')[0].get('name') if movie_data.get('production_countries') != [] else '',
            })
        
        return JsonResponse({'message':'SUCCESS', 'result':result}, status=200)

# tmdb
class MovieSearchView(APIView):
    def get(self, request):
        query       = request.GET.get('q')
        request_url = tmdb_helper.get_request_url(method='/search/movie', language='ko-KR', query=query)
        movies      = requests.get(request_url).json()
        result      = []
        
        for movie in movies.get('results',[]):
            
            movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie['id']), region='KR', language='ko-KR')
            movie_data_raw_data = requests.get(movie_data_request_url)
            movie_data = movie_data_raw_data.json()
            
            result.append({
                'id'           : movie['id'],
                'title'        : movie['title'],
                'en_title'     : movie['original_title'],
                'running_time' : movie_data.get('runtime'),
                'release_date' : movie.get('release_date', ''),
                'country'      : movie_data.get('production_countries')[0].get('name') if movie_data.get('production_countries') != [] else '',
                'poster'       : TMDB_IMAGE_BASE_URL+movie['poster_path'] if movie['poster_path'] else '' 
            })
        
        return JsonResponse({'message':'SUCCESS', 'result':result}, status = 200)

#tmdb
class ActorSearchView(APIView):
    def get(self, request):
        query       = request.GET.get('q')
        request_url = tmdb_helper.get_request_url(method='/search/person', language='ko-KR', query=query)
        people      = requests.get(request_url).json()
        result      = []
        
        for person in people.get('results',[]):
            
            person_data_request_url = tmdb_helper.get_request_url(method='/person/'+str(person['id']), language='ko-KR', region='KR')
            person_data_raw_data = requests.get(person_data_request_url)
            person_data = person_data_raw_data.json()
            
            result.append({
                'id'            : person['id'],
                'name'          : person_data.get('name', ''),
                'profile_image' : TMDB_IMAGE_BASE_URL+person.get('profile_path') if person.get('profile_path') != None else '',
                'known_for'     : [{'id':i.get('id'), 'title': i.get('title','')} for i in person.get('known_for',[])[:2]],
                'department'    : person.get('known_for_department')
            })
        
        return JsonResponse({'message':'SUCCESS', 'result':result}, status = 200)

class ActorDetailView(APIView):
    def get(self, request):
        actor_id = request.GET.get('actor_id')
        page     = int(request.GET.get('page', 0))
        limit    = int(request.GET.get('limit', 8))
        offset   = page*limit
        
        # PERSONS / Get Details
        person_data_request_url = tmdb_helper.get_request_url(method='/person/'+str(actor_id), language='ko-KR')
        person_data_raw_data    = requests.get(person_data_request_url)
        actor                   = person_data_raw_data.json()
        
        # PERSONS / Get Movie Credits
        person_movie_credits_data_request_url = tmdb_helper.get_request_url(method='/person/'+str(actor_id)+'/movie_credits', language='ko-KR')
        person_movie_credits_data_raw_data    = requests.get(person_movie_credits_data_request_url)
        actor_movie                           = person_movie_credits_data_raw_data.json()
        
        total_page = -1
                
        if actor_movie.get('success') == False:
            actor_data = {
                'total_page' : total_page,
                'name'       : actor.get('name'),
                'image_url'  : TMDB_IMAGE_BASE_URL+actor.get('profile_path') if actor.get('profile_path') != None else '',
                'country'    : actor.get('place_of_birth'),
                'starring_list' : []
            }
            return Response({'actor_info': actor_data}, status=200)
        
        total_movie = len(actor_movie['cast'])      
        total_page  = ((total_movie)//limit)-1 if total_movie%limit == 0 else (total_movie//limit)
        
        if 'Authorization' in request.headers: #로그인 된 상태
            try:
                token               = request.headers.get("Authorization")
                payload             = jwt.decode(token, SECRET_KEY, ALGORITHM)  
                user                = User.objects.get(id=payload["id"])
                movies_with_reviews = [movie['movie_id'] for movie in Review.objects.filter(user=user).values('movie_id')]
                intimacy            = 0
                
                actor_data = {
                    'total_page' : total_page,
                    'name'       : actor.get('name'),
                    'image_url'  : TMDB_IMAGE_BASE_URL+actor.get('profile_path') if actor.get('profile_path') != None else '',
                    'country'    : actor.get('place_of_birth'),
                    'starring_list' : [{
                        'id'                   : movie.get('id'),
                        'title'                : movie.get('title'),
                        'release'              : movie.get('release_date').split("-")[0],
                        'thumbnail_image_url'  : TMDB_IMAGE_BASE_URL+movie.get('poster_path') if movie.get('poster_path') != None else '',
                        'role_name'            : movie.get('character'),
                        'ratings'              : {'review':True, 'rating':Review.objects.get(user=user,movie_id=movie.get('id')).rating} if str(movie.get('id')) in movies_with_reviews else {'review':False, 'rating':round(float(movie.get('vote_average'))/2,0)},
                        'platform'             : TMDB_IMAGE_BASE_URL + requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy')[0].get('logo_path') \
                                                 if requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results') != None \
                                                     and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR') != None \
                                                     and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy') != None \
                                                     and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy')[0].get('logo_path') != None
                                                 else '',
                        'background_image_url' : TMDB_IMAGE_BASE_URL + requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')[0].get('file_path') \
                                                 if len(requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')) > 0 and \
                                                    requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')[0].get('file_path') != None
                                                 else ''
                        } for movie in sorted(actor_movie.get('cast'), key=lambda x:x.get('release_date'), reverse=True)[offset:offset+limit]],                
                }
                movie_ids = [actor.get('id') for actor in actor_movie.get('cast')]
                
                for review_id in movies_with_reviews:
                    if int(review_id) in movie_ids:
                        intimacy += 1
                
                actor_data['intimacy']    = intimacy
                actor_data['total_movie'] = total_movie
                
                return Response({'actor_info':actor_data}, status=200)
            
            except User.DoesNotExist:                                           
                pass
            
            except jwt.exceptions.ExpiredSignatureError:
                pass
            
            except jwt.exceptions.DecodeError:                                     
                pass
                
        actor_data = {
            'total_page' : total_page,
            'name'       : actor.get('name'),
            'image_url'  : TMDB_IMAGE_BASE_URL+actor.get('profile_path') if actor.get('profile_path') != None else '',
            'country'    : actor.get('place_of_birth'),
            'starring_list' : [{
                'id'                   : movie.get('id'),
                'title'                : movie.get('title'),
                'release'              : movie.get('release_date').split("-")[0],
                'thumbnail_image_url'  : TMDB_IMAGE_BASE_URL+movie.get('poster_path') if movie.get('poster_path') != None else '',
                'role_name'            : movie.get('character'),
                'ratings'              : round(float(movie.get('vote_average'))/2,0),
                'platform'             : TMDB_IMAGE_BASE_URL + requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy')[0].get('logo_path') \
                                         if requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results') != None \
                                             and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR') != None \
                                             and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy') != None \
                                             and requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/watch/providers')).json().get('results').get('KR').get('buy')[0].get('logo_path') != None
                                         else '',
                'background_image_url' : TMDB_IMAGE_BASE_URL + requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')[0].get('file_path') \
                                        if len(requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')) > 0 and \
                                            requests.get(tmdb_helper.get_request_url(method='/movie/'+str(movie.get('id'))+'/images')).json().get('backdrops')[0].get('file_path') != None
                                        else ''
                } for movie in sorted(actor_movie.get('cast'), key=lambda x:x.get('release_date'), reverse=True)[offset:offset+limit]]
        }

        return Response({'actor_info': actor_data}, status=200)