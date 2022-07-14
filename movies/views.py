import random

from django.http             import JsonResponse
from django.views            import View
from django.db.models        import Avg
from rest_framework.views    import APIView
from rest_framework.response import Response
from datetime                import datetime
from django.db               import transaction
from django.db.models        import Q

from .models                import *
from users.models           import User
from reviews.models         import Review
from users.models           import ProfileImage
from my_settings            import AWS_S3_URL
from core.storages          import s3_client, FileHander
from core.utils             import login_decorator

class MovieDetailView(APIView):
    def get(self, request, movie_id):
        try:
            movie          = Movie.objects.get(id=movie_id)
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
                'platform_name'       : MoviePlatform.objects.get(movie_id=movie.id).platform.name,
                'platform_logo_image' : AWS_S3_URL+MoviePlatform.objects.get(movie_id=movie.id).platform.image_url,
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
            
            return Response({'movie_info': movie_data}, status=200)
        
        except Movie.DoesNotExist:
            return Response({'message': 'MOVIE_NOT_EXIST'}, status=400)

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
    
class MovieSearchView(View):
    def get(self, request):
        try:
            q = request.GET.get('q')
            
            query = Q()
            query |= Q(title__icontains=q)
            query |= Q(en_title__icontains=q)
            #쿼리를 통해 정참조하고있는 다른 테이블의 데이터를 검증하는 조건을 더할 것 - country
            
            movie_list = Movie.objects.filter(query).distinct()
            
            result = [
                {
                    'movie_id'     : movie.id,
                    'title'        : movie.title,
                    'en_title'     : movie.en_title,
                    'running_time' : movie.running_time,
                    'release_date' : movie.release_date,
                    'country'      : movie.country.name,
                    'poster'       : AWS_S3_URL+ThumbnailImage.objects.get(movie_id=movie.id).image.image_url
                } for movie in movie_list]
            
            return JsonResponse({'message':'SUCCESS', 'result':result}, status = 200)
        
        except Movie.DoesNotExist:
            
            return Response({'message': 'MOVIE_NOT_EXIST'}, status=400)
  
class ActorDetailView(APIView):
    def get(self, request, actor_id):
        try:
            actor            = Actor.objects.get(id=actor_id)
            movie_actor_list = MovieActor.objects.filter(actor_id=actor_id)
            job_list         = ActorJob.objects.filter(actor_id=actor_id)
            movie_list       = Movie.objects.filter().order_by('-release_date')
            list = []

            for movie in movie_list:
                [list.append(movie_actor.movie_id) for movie_actor in MovieActor.objects.filter(actor_id=actor_id, movie_id=movie.id)]
            
            image_list = [movie_image.image.image_url for movie_image in MovieImage.objects.filter(movie_id=list[0])]
            
            actor_data = {
                'id'               : actor.id,
                'name'             : actor.name,
                'image_url'        : AWS_S3_URL+actor.image.image_url,
                'country'          : actor.country.name,
                'birth'            : datetime.strftime(actor.birth, '%Y년 %m월 %d일'),
                'debut'            : actor.debut,
                'debut_year'       : '' if actor.debut_year==0 else str(actor.debut_year)+'년',
                'height'           : '' if actor.height==0 else str(actor.height)+'cm ',
                'weight'           : '' if actor.weight==0 else str(actor.weight)+'kg',
                'job'              : [job.job.name for job in job_list],
                'background_image' : AWS_S3_URL+random.choice(image_list),
                'agency'           : actor.agency,
                'starring_list'    : [{
                    'movie_id'            : movie_actor.movie.id,
                    'title'               : movie_actor.movie.title,
                    'release'             : datetime.strftime(movie_actor.movie.release_date, '%Y'),
                    'thumbnail_image_url' : AWS_S3_URL+ThumbnailImage.objects.get(movie_id=movie_actor.movie.id).image.image_url,
                    'movie_image_url'     : AWS_S3_URL+random.choice([movie_image.image.image_url for movie_image in MovieImage.objects.filter(movie_id=movie_actor.movie_id)]) if [movie_image.image.image_url for movie_image in MovieImage.objects.filter(movie_id=movie_actor.movie_id)] else '',
                    'role_name'           : movie_actor.role.name,
                    'ratings'             : str(float(Review.objects.filter(movie_id=movie_actor.movie.id).aggregate(Avg('rating'))['rating__avg'])) if Review.objects.filter(movie_id=movie_actor.movie.id).aggregate(Avg('rating'))['rating__avg'] else "0",
                    'platform'            : MoviePlatform.objects.get(movie_id=movie_actor.movie.id).platform.name,
                    'platform_logo_image' : AWS_S3_URL+MoviePlatform.objects.get(movie_id=movie_actor.movie.id).platform.image_url,
                    } for movie_actor in movie_actor_list]
            }
            
            return Response({'actor_info': actor_data}, status=200)
        
        except Actor.DoesNotExist:
            return Response({'message': 'ACTOR_NOT_EXIST'}, status=400)
        
    @transaction.atomic(using='default')
    def post(self, request):
        try:
            data         = request.data
            name         = data['name']
            image_url    = data['image_url']
            country_id   = data['country_id']
            birth        = data['birth']
            debut        = data['debut']
            debut_year   = data['debut_year']
            height       = data.get('height', 0)
            weight       = data.get('weight', 0)
            job_id_list  = data.getlist('job_id')
            
            if Actor.objects.filter(name=name, birth=birth):
                return Response({'message': 'ALREADY_ACTOR'}, status=400)
            
            else:
                image_url = FileHander(s3_client).upload(image_url, 'image/actor')
                image     = Image.objects.create(image_url=image_url)
                
                actor = Actor.objects.create(
                    name       = name,
                    image      = image,
                    country    = Country.objects.get(id=country_id),
                    birth      = birth,
                    debut      = debut,
                    debut_year = debut_year,
                    height     = height,
                    weight     = weight,
                )
                
                ActorJob.objects.bulk_create([
                    ActorJob(actor = actor,
                             job   = Job.objects.get(id=job_id)
                ) for job_id in job_id_list])
            
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
    

class ActorIntimacyView(APIView):
    @login_decorator
    def get(self, request, actor_id):
        user = request.user
        
        total_count  = MovieActor.objects.filter(actor_id=actor_id).count()
        viewed_count = len([MovieActor.objects.filter(movie_id=review.movie_id, actor_id=actor_id)
                       for review in Review.objects.filter(user_id=user.id)])

        if total_count==0:
            return Response({'message': 'ACTOR_NOT_EXIST'}, status=400)
        
        intimacy_info = {
            'total_count'  : total_count,
            'viewed_count' : viewed_count,
        }
        
        return Response({'intimacy_info': intimacy_info}, status=200)
    
    
class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        
        data = [{
            'title'        : movie.title,    
            'en_title'     : movie.en_title,    
            'running_time' : movie.running_time,    
            'ratings'      : '미구현',
            'country'      : movie.country.name,    
            'genre'        : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie.id)],    
            'release_date' : movie.release_date,    
            'category'     : movie.category.name,        
        } for movie in movies]
        
        return Response({'message': data}, status=200)