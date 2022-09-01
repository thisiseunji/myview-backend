#movies.views.py

import requests, random

from django.http             import JsonResponse
from django.views            import View
from rest_framework.views    import APIView
from rest_framework.response import Response

from reviews.models         import Review
from users.models           import ProfileImage
from my_settings            import AWS_S3_URL, TMDB_IMAGE_BASE_URL, TMDB_VIDEO_BASE_URL
from core.storages          import s3_client, FileHander
from core.utils             import login_decorator
from core.tmdb              import tmdb_helper


#tmdb 수정
class MovieDetailView(APIView):
    def get(self, request, movie_id):
        # MOVIES / Get Details
        movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id), region='KR', language='ko')
        movie_data_raw_data = requests.get(movie_data_request_url)
        movie_data = movie_data_raw_data.json()
        
        # MOVIES / Get credits
        actor_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie_id)+'/credits', language='ko')
        actor_data_raw_data = requests.get(actor_data_request_url)
        actor_data = actor_data_raw_data.json()
        
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
        
        if movie_data.get('id') == None :
            return Response('{message : INVALID_DATA}', status=404)
        
        movie_data = {
            'id'                  : movie_data.get('id'),
            'title'               : movie_data.get('title'),
            'en_title'            : movie_data.get('original_title'),
            'description'         : movie_data.get('overview'),
            'running_time'        : movie_data.get('runtime'),
            'age'                 : '미구현 adult: true or false',
            'ratings'             : movie_data.get('vote_average'),
            'release_date'        : movie_data.get('release_date'),
            'country'             : movie_data.get('production_countries')[0].get('name') if movie_data.get('production_countries') != None else '',
            'category'            : '미구현 제공여부 확인중',
            'genre'               : [genre.get('name') for genre in movie_data.get('genres')] if movie_data.get('genres') != None else '',
            'platform_name'       : [provider.get('provider_name') for provider in provider_data.get('results').get('KR').get('buy')] if provider_data.get('results') != None and provider_data.get('results').get('KR') != None and provider_data.get('results').get('KR').get('buy') != None else '',
            'platform_logo_image' : [TMDB_IMAGE_BASE_URL+provider.get('logo_path') for provider in provider_data.get('results').get('KR').get('buy')] if provider_data.get('results') != None and provider_data.get('results').get('KR') != None and provider_data.get('results').get('KR').get('buy') != None else '',
            'actor'               : [{
                'id'        : actor.get('id'),
                'name'      : actor.get('name'),
                'country'   : '미구현 제공여부 확인중',
                'image'     : actor.get('profile_path'),
                'role'      : '미구현 제공여부 확인중',
                'role_name' : 'character',
                } for actor in actor_data.get('cast')] if actor_data.get('cast') != None else '',  
            'thumbnail_image_url' : TMDB_IMAGE_BASE_URL+movie_data.get('poster_path') if movie_data.get('poster_path') != None else '',
            'image_url'           : [TMDB_IMAGE_BASE_URL+image.get('file_path') for image in image_data.get('backdrops')] if image_data.get('backdrops') != None else '',
            'video_url'           : [TMDB_VIDEO_BASE_URL+video.get('key') for video in video_data.get('results')] if video_data.get('results') != None else '',
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


# tmdb
class MovieSearchView(APIView):
    def get(self, request):
        query       = request.GET.get('q')
        request_url = tmdb_helper.get_request_url(method='/search/movie', language='ko-KR', query=query)
        movies      = requests.get(request_url).json()
        result      = []
        
        for movie in movies.get('results',[]):
            
            movie_data_request_url = tmdb_helper.get_request_url(method='/movie/'+str(movie['id']), region='KR', language='ko')
            movie_data_raw_data = requests.get(movie_data_request_url)
            movie_data = movie_data_raw_data.json()
            
            result.append({
                'movie_id'     : movie['id'],
                'title'        : movie['title'],
                'en_title'     : movie['original_title'],
                'running_time' : movie_data.get('runtime'),
                'release_date' : movie.get('release_date', ''),
                'country'      : movie_data.get('production_countries')[0].get('name') if movie_data.get('production_countries') != [] else '',
                'poster'       : TMDB_IMAGE_BASE_URL+movie['poster_path'] if movie['poster_path'] else '' 
            })
        
        return JsonResponse({'message':'SUCCESS', 'result':result}, status = 200)


# class ActorIntimacyView(APIView):
#     @login_decorator
#     def get(self, request, actor_id):
        
#         user = request.user
        
#         data = [{
#             'movie_id': review.movie_id,
#             'rating' : review.rating,
#             } for review in Review.objects.filter(user_id=user)]
        
#         return Response({'data': data}, status=200)