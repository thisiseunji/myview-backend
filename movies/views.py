from django.http             import JsonResponse
from django.views            import View
from django.db               import transaction
from django.db.models        import Avg
from rest_framework.views    import APIView
from rest_framework.response import Response
from my_settings             import AWS_S3_URL

from .models                import *
from reviews.models         import Review

class MovieDetailView(APIView):       
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            
            movie_info = {
                'title'               : movie.title,
                'en_title'            : movie.en_title,
                'description'         : movie.description,
                'running_time'        : movie.running_time,
                'age'                 : movie.age,
                'ratings'             : str(float(Review.objects.filter(movie_id=movie.id).aggregate(Avg('rating'))['rating__avg'])),
                'release_date'        : movie.release_date,
                'country'             : movie.country.name,
                'category'            : movie.category.name,
                'genre'               : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie_id)],
                'actor'               : [{'id'        : movie_actor.actor.id,
                                          'name'      : movie_actor.actor.name,
                                          'country'   : movie_actor.actor.country.name,
                                          'image'     : AWS_S3_URL+movie_actor.actor.image.image_url,
                                          'role'      : movie_actor.role.name,
                                          'role_name' : movie_actor.role_name,
                                          } for movie_actor in MovieActor.objects.filter(movie_id=movie_id)],  
                'thumbnail_image_url' : AWS_S3_URL+ThumbnailImage.objects.get(movie_id=movie_id).image.image_url,
                'image_url'           : [AWS_S3_URL+image.image.image_url for image in MovieImage.objects.filter(movie_id=movie_id)],
                'video_url'           : [AWS_S3_URL+video.video.video_url for video in MovieVideo.objects.filter(movie_id=movie_id)],
                }
            
            return JsonResponse({'movie_info': movie_info}, status=200)
        
        except Movie.DoesNotExist:
            return JsonResponse({'message': 'MOVIE_NOT_EXIST'}, status=400)


class SimpleSearchView(View):
    def get(self, request):
        movies = Movie.objects.all()
        latest = movies.order_by('-release_date', 'title', 'id')[:10]
        titles = []
        rank   = []
        
        for movie in movies:
            titles.append({
                'id'    : movie.id,
                'title' : movie.title
            })
        
        for movie in latest:
            rank.append({
                'id'    : movie.id,
                'title' : movie.title
            })
        
        return JsonResponse({'message' : 'SUCCESS', 'rank' : rank, 'titles' : titles}, status=200)