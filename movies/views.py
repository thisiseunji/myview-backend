from django.http            import JsonResponse
from django.views           import View
from rest_framework.views   import APIView

from movies.models          import *
from users.models           import User


class MovieDetailView(APIView):
    def post(self, request):
        # try:
            data            = request.data
            title           = data['title']
            description     = data['description']
            release_date    = data['release_date']
            country         = data['country']
            category        = data['category']
            # genre           = data['genre']
            # actor           = data['actor']
            # actor_name      = data['actor_name']
            # actor_role      = data['actor_role']
            # actor_role_name = data['actor_role_name']
            # thumbnail_image = data['thumbnail_image']
            # movie_gallery   = data['movie_gallery']
            # movie_video     = data['movie_video']
            
            movie = Movie.objects.create(
                title        = title,
                description  = description,
                release_date = release_date,
                country      = country,
                category     = category,
            )
            
            return JsonResponse({'data': movie}, status=201)
            
    
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            
            data = {
                    'title'           : movie.title,
                    'description'     : movie.description,
                    'release_date'    : movie.release_date,
                    'country'         : movie.country.name,
                    'category'        : movie.category.name,
                    'genre'           : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie_id)],
                    'actor'           : [{'id'        : movie_actor.actor.id,
                                          'name'      : movie_actor.actor.name,
                                          'role'      : movie_actor.role.name,
                                          'role_name' : movie_actor.role_name,
                                          } for movie_actor in MovieActor.objects.filter(movie_id=movie_id)],  
                    'thumbnail_image' : ThumbnailImage.objects.get(movie_id=movie_id).image.image_url,
                    'movie_image'     : [image.image.image_url for image in MovieImage.objects.filter(movie_id=movie_id)]
                    }
            
            return JsonResponse({'data': data}, status=200)
        
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