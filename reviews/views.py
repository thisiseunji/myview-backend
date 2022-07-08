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
    def get(self, request, review_id):
        try:
            user   = request.user
            review = Review.objects.get(id=review_id)
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
                        'name' : ReviewPlace.objects.get(review_id=review_id).place.name,
                        'mapx' : ReviewPlace.objects.get(review_id=review_id).place.mapx,
                        'mapy' : ReviewPlace.objects.get(review_id=review_id).place.mapy,
                        'link' : ReviewPlace.objects.get(review_id=review_id).place.link   
                } if ReviewPlace.objects.filter(review_id=review_id).exists() else [],
                'tags'          : [
                    {
                        'tag'   : review_tag.tag.name, 
                        'color' : ColorCode.objects.get(id=randrange(0,4))
                    } for review_tag in ReviewTag.objects.filter(review=review)],
                'movie'         : {
                    'id'       : review.movie.id,
                    'title'    : review.movie.title,
                    'country'  : review.movie.country.name,
                    'category' : review.movie.category.name,
                }
            }
        
            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
        
    @login_decorator
    @transaction.atomic(using='default')
    def post(self, request):
        try:
            data   = request.data
            
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
            print(tags)
            
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
            print(data)
            for key in data.dict().keys():
                print(key)
                if key == 'place':
                    place = data['key']
                    print(data[key]) 
                    print(type(data[key]))
                    print(place['mapx'])
                    print(place['mapy'])
                    print(place['name'])
                    print(place['link'])
                    place, is_created = Place.objects.get_or_create(
                        mapx     = place['mapx'],
                        mapy     = place['mapy'],
                        defaults = {
                            'name' : place['name'],
                            'link' : place['link']
                        }
                    )
                    ReviewPlace.get_or_creat(
                        review = review,
                        place  = place
                    )
                    print(is_created)
                    
                if key == 'tags':
                    print(data[key])
                    print(type(data[key]))
                    for tag_name in data['tags'].split(','):
                        tag = Tag.objects.get_or_create(name=tag_name.strip())
                        ReviewTag.objects.create(
                            review = review,
                            tag    = tag[0]
                        )
                    
                if key == 'review_images_url' and data['review image_url'] not in ['', None]:
                    print(data[key])
                    print(type(data[key]))
                    file_handler      = FileHander(s3_client)
                    review_images_url = data['review_images_url']
                    review_images     = [review_image.image for review_image in ReviewImage.objects.filter(review_id=review.id)]

                    for review_image in review_images:
                        if AWS_S3_URL+review_image.image_url in review_images_url:
                            continue
                        else:
                            file_handler.delete(review_image.image_url)
                            review_image.delete()

                if key == 'review_images':
                    print(data[key])
                    print(type(data[key]))
                    file_handler = FileHander(s3_client)
                    for review_image in data['review_images']:

                        file_name = file_handler.upload(review_image,'image/review')
                        print(f'file_name:{file_name}')
                        image     = Image.objects.create(image_url=file_name)
                        print(f'images:{image}')

                        ReviewImage.objects.create(
                            image  = image,
                            review = review,
                        )
                if key == 'watched_date':
                    print(data[key])
                    print(type(data[key]))
                    print(data['watched_date'].split(' ')[0])
                    print(type(data['watched_date'].split(' ')[0]))
                    review.watched_date = data['watched_date'].split(' ')[0],
                    review.watched_time = data['watched_date'].split(' ')[1],
                
                if key == 'title':
                    print(data[key])
                    print(type(data[key]))
                    review.title = data[key]

                if key == 'content':
                    print(data[key])
                    print(type(data[key]))               
                    review.content = data[key]
                
                if key == 'with_user':
                    print(data[key])
                    print(type(data[key]))                
                    review.with_user = data[key]
                
                if key == 'rating':
                    print(data[key])
                    print(type(data[key]))
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
                    'poster'   : ThumbnailImage.objects.get(movie=review.movie).image.image_url,
                    'title'    : review.movie.title,
                    'en_title' : review.movie.en_title,
                    'released' : review.movie.release_date,
                    'country'  : review.movie.country.name,
                    'genre'    : [movie.genre.name for movie in MovieGenre.objects.filter(movie=review.movie)],
                    'age'      : review.movie.age,
                }
            } for review in reviews]
            
            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
            
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
