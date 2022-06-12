from django.http             import JsonResponse
from django.views            import View
from django.db               import transaction
from rest_framework.views    import APIView
from rest_framework.response import Response

from .models                import *
from .serializers           import MovieSerializer, ActorSerializer
from users.models           import User


class MovieDataView(APIView):
    @transaction.atomic(using='default')
    def post(self, request):
        # try:
            data                = request.data
            title               = data['title']
            description         = data['description']
            release_date        = data['release_date']
            
            country             = Country.objects.get(name=data['country_name'])
            category            = Category.objects.get(name=data['category_name'])
            genre               = Genre.objects.get(name=data['genre_name'])
            platform            = Platform.objects.get(name=data['platform_name'])
            
            actor               = Actor.objects.get(name=data['actor_name'])
            actor_role          = Role.objects.get(name=data['actor_role'])
            actor_role_name     = data['actor_role_name']
            
            thumbnail_image_url = data['thumbnail_image_url']
            movie_gallery_url   = data['movie_gallery_url']
            movie_video_url     = data['movie_video_url']
            
            
            movie = Movie.objects.create(
                title        = title,
                description  = description,
                release_date = release_date,
                country_id   = country.id,
                category_id  = category.id,
            )
            
            movie_gallery = Image.objects.create(
                image_url = movie_gallery_url
            )
            
            MovieImage.objects.create(
                movie = movie,
                image = movie_gallery
            )
            
            thumbnail_image = Image.objects.create(
                image_url = thumbnail_image_url
            )
            
            ThumbnailImage.objects.create(
                movie = movie,
                image = thumbnail_image
            )
            
            movie_video = Video.objects.create(
                video_url = movie_video_url
            )
            
            MovieVideo.objects.create(
                movie = movie,
                video = movie_video
            )
            
            MovieGenre.objects.create(
                movie = movie,
                genre = genre,
            )
            
            MoviePlatform.objects.create(
                movie = movie,
                platform = platform
            )
            
            MovieActor.objects.create(
                movie     = movie,
                actor     = actor,
                role      = actor_role,
                role_name = actor_role_name
            )
            
            serializer = MovieSerializer(instance=movie)
            return Response(serializer.data, status=201)
        
    def delete(self, request):
        try:
            movie_id_list = request.GET.getlist('movie_id')

            for movie_id in movie_id_list:
                Movie.objects.get(id=movie_id).delete()

            return Response({'message': 'DELETE_SUCCESS'}, status=204)
        
        except Movie.DoesNotExist:
            return Response({'message': 'MOVIE_NOT_EXIST'}, status=400)
        
        
class MovieDetailView(APIView):       
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            
            movie_info = {
                'title'               : movie.title,
                'description'         : movie.description,
                'release_date'        : movie.release_date,
                'country'             : movie.country.name,
                'category'            : movie.category.name,
                'genre'               : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie_id)],
                'actor'               : [{'id'        : movie_actor.actor.id,
                                          'name'      : movie_actor.actor.name,
                                          'country'   : movie_actor.actor.country.name,
                                          'image'     : movie_actor.actor.image.image_url,
                                          'role'      : movie_actor.role.name,
                                          'role_name' : movie_actor.role_name,
                                          } for movie_actor in MovieActor.objects.filter(movie_id=movie_id)],  
                'thumbnail_image_url' : ThumbnailImage.objects.get(movie_id=movie_id).image.image_url,
                'image_url'           : [image.image.image_url for image in MovieImage.objects.filter(movie_id=movie_id)],
                'video_url'           : [video.video.video_url for video in MovieVideo.objects.filter(movie_id=movie_id)],
                }
            
            return JsonResponse({'movie_info': movie_info}, status=200)
        
        except Movie.DoesNotExist:
            return JsonResponse({'message': 'MOVIE_NOT_EXIST'}, status=400)


class MovieTitleView(View):
    def get(self, request):
        data = []
        movies = Movie.objects.all()
        for i in movies:
            data.append({
                'id'    : i.id,
                'title' : i.title
            })
        return JsonResponse({'message' : 'SUCCESS', 'data': data}, status=200)
    
    
class ActorDataView(APIView):
    def post(self, request):
        try:
            actor_name = request.data['actor_name']
            country    = Country.objects.get(name=request.data['country_name'])
            image_url  = request.data['image_url']

            if Actor.objects.filter(name=actor_name):
                return Response({'message': 'ACTOR_IS_ALREADY_REGISTERED'}, status=400)

            else: 
                image = Image.objects.create(image_url=image_url)

                Actor.objects.create(
                    name    = actor_name,
                    country = country,
                    image   = image,
                )

                return Response({'message': 'CREATE_SUCCESS'}, status=201)
        
        except KeyError:
            return Response({'message': 'KEY_ERROR'}, status=400)
        
    def get(self, request):
        actors = Actor.objects.all()
        actor_list = [actor.name for actor in actors]
        
        return Response({'actor_list': actor_list}, status=200)
    
    def patch(self, request):
        try:
            data         = request.data
            actor_id     = data['actor_id']
            actor_name   = data.get('actor_name')
            country_name = data.get('country_name')
            image_url    = data.get('image_url')

            actor = Actor.objects.get(id=actor_id)
            image = actor.image
             
            if actor_name:
                actor.name = actor_name
            if country_name:
                actor.country_id = Country.objects.get(name=country_name)
            if image_url:
                image.image_url = image_url
                image.save()
                
            with transaction.atomic():
                actor.save()

            return Response({'message': 'ACTOR_UPDATE_SUCCESS'}, status=201)
        
        except Actor.DoesNotExist:
            return Response({'message': 'ACTOR_NOT_EXIST'}, status=400)
        
        except KeyError:
            return Response({'message': 'KEY_ERROR'}, status=400)
        
    def delete(self, request):
        try:
            actor_id_list = request.GET.getlist('actor_id')

            for actor_id in actor_id_list:
                Actor.objects.get(id=actor_id).delete()

            return Response({'message': 'DELETE_SUCCESS'}, status=204)
        
        except Actor.DoesNotExist:
            return Response({'message': 'ACTOR_NOT_EXIST'}, status=400)