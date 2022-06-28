from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Avg
from rest_framework.views    import APIView
from rest_framework.response import Response
from datetime                import datetime
from django.db               import transaction

from .models                import *
from reviews.models         import Review
from .serializers           import MovieSerializer
from my_settings            import AWS_S3_URL
from core.storages          import s3_client, FileHander

class MovieDetailView(APIView):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            review_ratings = Review.objects.filter(movie_id=movie.id).aggregate(Avg('rating'))['rating__avg']
            
            movie_data = {
                'id'                  : movie.id,
                'title'               : movie.title,
                'en_title'            : movie.en_title,
                'description'         : movie.description,
                'running_time'        : movie.running_time,
                'age'                 : movie.age,
                'ratings'             : str(float(review_ratings)) if review_ratings else 0,
                'release_date'        : movie.release_date,
                'country'             : movie.country.name,
                'category'            : movie.category.name,
                'genre'               : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie_id)],
                'actor'               : [{
                    'id'        : movie_actor.actor.id,
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
            
            movie_serializer = MovieSerializer(instance=movie_data)
            
            return Response({'movie_info': movie_serializer.data}, status=200)
        
        except Movie.DoesNotExist:
            return Response({'message': 'MOVIE_NOT_EXIST'}, status=400)


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
    
    
class ActorDetailView(APIView):
    def get(self, request, actor_id):
        try:
            actor      = Actor.objects.get(id=actor_id)
            movie_list = MovieActor.objects.filter(actor_id=actor_id)
            job_list   = ActorJob.objects.filter(actor_id=actor_id)
            
            actor_data = {
                'id'            : actor.id,
                'name'          : actor.name,
                'image_url'     : AWS_S3_URL+actor.image.image_url,
                'country'       : actor.country.name,
                'birth'         : actor.birth,
                'debut'         : actor.debut,
                'debut_year'    : actor.debut_year,
                'height'        : actor.height,
                'weight'        : actor.weight,
                'job'           : [job.job.name for job in job_list],
                'starring_list' : [{
                    'title'               : movie.movie.title,
                    'release'             : datetime.strftime(movie.movie.release_date, '%Y'),
                    'thumbnail_image_url' : AWS_S3_URL+ThumbnailImage.objects.get(movie_id=movie.movie.id).image.image_url,
                    'role_name'           : movie.role.name,
                    'ratings'             : str(float(Review.objects.filter(movie_id=movie.movie.id).aggregate(Avg('rating'))['rating__avg'])) if Review.objects.filter(movie_id=movie.movie.id).aggregate(Avg('rating'))['rating__avg'] else "0",
                    'platform'            : MoviePlatform.objects.get(movie_id=movie.movie.id).platform.name,
                    'platform_logo_image' : AWS_S3_URL+MoviePlatform.objects.get(movie_id=movie.movie.id).platform.image_url,
                    } for movie in movie_list]
            }
            
            return Response({'actor_info': actor_data}, status=200)
        
        except Actor.DoesNotExist:
            return Response({'message': 'ACTOR_NOT_EXIST'}, status=400)
        
    @transaction.atomic(using='default')
    def post(self, request):
        try:
            data         = request.data
            actor_name   = data['actor_name']
            country_name = data['country_name']
            image_url    = data['image_url']
            
            if Actor.objects.filter(name=actor_name):
                return Response({'message': 'ALREADY_ACTOR'}, status=400)
            
            else:
                country = Country.objects.get(name=country_name)

                image_url = FileHander(s3_client).upload(image_url, 'image/actor')
                image = Image.objects.create(image_url=image_url)
            
                Actor.objects.create(
                    name    = actor_name,
                    country = country,
                    image   = image
                )
            
                return Response({'message': 'CREATE_SUCCESS'}, status=201)
            
        except KeyError:
            return Response({'message': 'KEY_ERROR'}, status=400)
        
    def patch(self, request):
        data         = request.data
        actor_id     = data['actor_id']
        actor_name   = data.get('actor_name')
        country_name = data.get('country_name')
        image_url    = data.get('image_url')
        
        actor = Actor.objects.get(id=actor_id)
        
        if actor_name:
            actor.name=actor_name
        if country_name:
            actor.country = Country.objects.get(name=country_name)
        if image_url:
            #* 기존 이미지 S3에서 삭제
            delete_image_url = actor.image.image_url
            FileHander(s3_client).delete(delete_image_url)
            #* 새로운 이미지 S3에 업로드 & db데이터 업데이트
            image_url = FileHander(s3_client).upload(image_url, 'image/actor')
            actor.image.image_url=image_url
            
        with transaction.atomic():
            actor.save()
            
        return Response({'message': 'ACTOR_UPDATE_SUCCESS'}, status=201)
        
        
class ActorListView(APIView):
    def get(self, request):
        actors = Actor.objects.all().order_by('name')
        
        actor_list = [{
            'id'       : actor.id,
            'name'     : actor.name,
            'country'  : actor.country.name,
            'image_url': AWS_S3_URL+actor.image.image_url
        } for actor in actors]
        
        return Response({'actor_list': actor_list}, status=200)