from random         import randrange
from django.http    import JsonResponse
from django.views   import View
from django.db      import transaction
from rest_framework.views import APIView

from core.utils     import login_decorator
from core.storages  import FileHander, s3_client
from movies.models  import Image, MovieGenre, ThumbnailImage
from reviews.models import ColorCode, Place, ReviewImage, ReviewPlace, Tag, Review, ReviewTag
from users.models   import User
from my_settings    import AWS_S3_URL

class ReviewView(APIView):
    @login_decorator
    def get(self, request, movie_id):
        try:
            user   = request.user
            review = Review.objects.get(user=user, movie_id=movie_id)
            result = { 
                'review_id'     : review.id,
                'title'         : review.title,
                'content'       : review.content,
                'rating'        : review.rating,
                'with_user'     : review.with_user,
                'watched_date'  : f'{review.watched_date} {review.watched_time}',
                'review_images' : [AWS_S3_URL+review_image.image.image_url for review_image in ReviewImage.objects.filter(review=review)],
                #값이 없을 경우 리턴 값 설정
                'place'         : {
                        'name' : ReviewPlace.objects.get(review=review).place.name,
                        'mapx' : ReviewPlace.objects.get(review=review).place.mapx,
                        'mapy' : ReviewPlace.objects.get(review=review).place.mapy,
                        'link' : ReviewPlace.objects.get(review=review).place.link   
                } if ReviewPlace.objects.filter(review_id=review).exists() else [],
                'tags'          : [
                    {
                        'tag'   : review_tag.tag.name, 
                        'color' : ColorCode.objects.get(id=randrange(0,4)).color_code
                    } for review_tag in ReviewTag.objects.filter(review=review)],
                'movie'         : {
                    'id'       : review.movie.id,
                    'title'    : review.movie.title,
                    'country'  : review.movie.country.name,
                    'category' : review.movie.category.name,
                }
            }
        
            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)

        except Review.DoesNotExist:
            return JsonResponse({'message' : 'REVIEW_DOSE_NOT_EXISTS'}, status=400)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
        
    @login_decorator
    @transaction.atomic(using='default')
    def post(self, request):
        try:
            data = request.data
            
            if Review.objects.filter(user=request.user, movie_id=data['movie_id']).exists():
                return JsonResponse({'message' : 'REVIEW_ALREADY_EXSISTS'}, status=403)
            
            review = Review.objects.create(
                user         = request.user,
                movie_id     = data['movie_id'],
                title        = data['title'],
                content      = data['content'],
                rating       = data['rating'],
                watched_date = data['watched_date'].split(' ')[0],
                watched_time = data['watched_date'].split(' ')[1],
                with_user    = data['with_user']
            )
            
            file_handler = FileHander(s3_client)
            
            review_images = data.getlist('review_images', None)
        
            if review_images:
                for review_image in review_images:
                    file_name = file_handler.upload(review_image,'image/review')
                    image     = Image.objects.create(image_url=file_name)
                    
                    ReviewImage.objects.create(
                        image  = image,
                        review = review,
                    )
            
            place_info = data.getlist('place', None)

            if place_info:
                place, is_created = Place.objects.update_or_create(
                    mapx = place_info[0],
                    mapy = place_info[1],
                    defaults = {
                        'name' : place_info[2],
                        'link' : place_info[3]
                    }
                )
                
                ReviewPlace.objects.create(place=place, review=review)
            
            tags = data.getlist('tags', None)
            
            if tags:
                for tag in tags:
                    tag, is_created = Tag.objects.get_or_create(name=tag)
                    ReviewTag.objects.create(
                        review = review,
                        tag    = tag
                    )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
                
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    @login_decorator
    @transaction.atomic(using='default')
    def put(self, request):
        try:
            data   = request.data
            review = Review.objects.get(id=data['review_id'])
            
            for key in data.dict().keys():
                
                if key == 'place':
                    place_info = data.getlist(key, None)
                
                    place, is_created = Place.objects.update_or_create(
                        mapx     = place_info[0],
                        mapy     = place_info[1],
                        defaults = {
                            'name' : place_info[2],
                            'link' : place_info[3]
                        }
                    )
                    ReviewPlace.objects.update_or_create(
                        review = review,
                        place  = place
                    )
                    
                if key == 'tags':
                    ReviewTag.objects.filter(review=review).delete()
                    for tag_name in data.getlist(key, None):
                        tag, is_created = Tag.objects.get_or_create(name=tag_name)
                        ReviewTag.objects.create(
                            review = review,
                            tag    = tag
                        )
                
                if key == 'review_images':
                    file_handler      = FileHander(s3_client)
                    review_image_urls = [review_image.image.image_url for review_image in ReviewImage.objects.filter(review_id=review.id)]
                    for review_image in data.getlist(key):
                        if type(review_image) != str:
                            file_name = file_handler.upload(review_image,'image/review')
                            image     = Image.objects.create(image_url=file_name)

                            ReviewImage.objects.create(
                                image  = image,
                                review = review,
                            )
                        
                        elif type(review_image) == str and review_image[len(AWS_S3_URL):] in review_image_urls:
                            review_image_urls.remove(review_image[len(AWS_S3_URL):])
                            
                    for review_image in review_image_urls:
                        file_handler.delete(review_image)
                        Image.objects.get(image_url=review_image).delete()
                
                if key == 'watched_date':
                    review.watched_date = data[key].split(' ')[0]
                    review.watched_time = data[key].split(' ')[1]
                    
                if key == 'title':
                    review.title = data[key]

                if key == 'content':
                    review.content = data[key]
                
                if key == 'with_user':
                    review.with_user = data[key]
                
                if key == 'rating':
                    review.rating = data[key]
            
            review.save()
               
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
                    
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
            
    @login_decorator
    def delete(self, request, review_id):
        try:
            review        = Review.objects.get(id=review_id, user=request.user)
            review_images = [review_image.image for review_image in ReviewImage.objects.filter(review=review)]
            
            file_handler = FileHander(s3_client)
            
            for review_image in review_images:
                file_handler.delete(review_image.image_url)
                review_image.delete()
            
            ReviewTag.objects.filter(review=review).delete()
            
            review.delete()

            return JsonResponse({'message':'NO_CONTENTS'}, status=204)
        
        except Review.DoesNotExist:
            return JsonResponse({'message':'REVIEW_NOT_EXIST'}, status=400)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)

class ReviewListView(View):
    @login_decorator
    def get(self, request):
        try:
            user    = request.user
            reviews = User.objects.get(id=user.id).review_set.all().order_by('-updated_at')
            result  = [{ 
                'review_id' : review.id,
                'title'     : review.title,
                'rating'    : review.rating,
                'movie'     : {
                    'id'       : review.movie.id,
                    'poster'   : AWS_S3_URL+ThumbnailImage.objects.get(movie=review.movie).image.image_url,
                    'title'    : review.movie.title,
                    'en_title' : review.movie.en_title,
                    'released' : review.movie.release_date,
                    'country'  : review.movie.country.name,
                    'genre'    : [movie.genre.name for movie in MovieGenre.objects.filter(movie=review.movie)],
                    'age'      : review.movie.age,
                    'running_time' : review.movie.running_time
                }
            } for review in reviews]
            
            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
            
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)

class ReviewTopThreeView(View):
    @login_decorator
    def get(self, request):
        reviews = Review.objects.filter(user=request.user).order_by('-rating', '-updated_at')[:3]
        
        if len(reviews) == 0 :
            return JsonResponse({'message' : 'NO_REVIEW'}, status=200)
        
        else:
            result = [{
                    'review_id' : reviews[i].id,
                    'title'     : reviews[i].title,
                    'rating'    : reviews[i].rating,
                    'movie'     : {
                        'id'     : reviews[i].movie_id,
                        'poster' : AWS_S3_URL+ThumbnailImage.objects.get(movie=reviews[i].movie).image.image_url,
                        'title'  : reviews[i].movie.title,
                        }
                } for i in range(len(reviews))]

            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)