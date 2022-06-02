from django.http            import JsonResponse
from rest_framework.views   import APIView

from movies.models          import Movie, MovieImage, ThumbnailImage, MovieActor, MovieGenre


class MovieDetailView(APIView):
    def get(self, request, movie_id):
        # try:
            movie           = Movie.objects.get(id=movie_id)
            
            data = {
                    'title'           : movie.title,
                    'description'     : movie.description,
                    'release_date'    : movie.release_date,
                    'country'         : movie.country.name,
                    'category'        : movie.category.name,
                    'genre'           : [movie_genre.genre.name for movie_genre in MovieGenre.objects.filter(movie_id=movie_id)],
                    'actor'           : [{'id': movie_actor.actor.id,
                                          'name':movie_actor.actor.name,
                                          'role_name': movie_actor.role_name,
                                          'role': movie_actor.role.name,
                                          } for movie_actor in MovieActor.objects.filter(movie_id=movie_id)],  
                    'thumbnail_image' : ThumbnailImage.objects.get(movie_id=movie_id).image.image_url,
                    'movie_image'     : [image.image.image_url for image in MovieImage.objects.filter(movie_id=movie_id)]
                    }
            
            return JsonResponse({'data':data})