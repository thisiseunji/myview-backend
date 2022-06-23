from random         import randrange
from django.http    import JsonResponse
from django.views   import View
from django.db      import transaction

from core.utils     import login_decorator
from core.storages  import FileHander, s3_client
from movies.models  import Image, MovieGenre, ThumbnailImage
from reviews.models import ColorCode, ReviewImage, Tag, Review, ReviewTag
from users.models   import User
from my_settings    import AWS_S3_URL

class ReviewView(View):
    @login_decorator
    def get(self, request):
        try:
            user    = request.user
            reviews = User.objects.get(id=user.id).reviews_set.all()
            result  = [
                { 
                    'review_id'     : review.id,
                    'title'         : review.title,
                    'content'       : review.content,
                    'rating'        : review.rating,
                    'with_user'     : review.with_user,
                    'watched_date'  : f'{review.watched_date} {review.watched_time}',
                    'review_images' : [AWS_S3_URL+review_image.image.image_url for review_image in ReviewImage.objects.filter(review=review)],
                    #값이 없을 경우 리턴 값 설정
                    'place '        : {
                            'name' : review.review_places.name,
                            'mapx' : review.review_places.mapx,
                            'mapy' : review.review_places.mapy,
                            'link' : review.review_places.link   
                    } if review.review_places.exists() else None,
                    'tags'          : [
                        {
                            'tag'   : review_tag.tag.name, 
                            'color' : ColorCode.objects.get(id=randrange(0,4))
                        } for review_tag in ReviewTag.objects.filter(review=review)],
                    'movie'         : {
                        'id'       : review.movie.id,
                        'title'    : review.movie.title,
                        'country'  : review.movie.country,
                        'category' : review.movie.category,
                    }
                } for review in reviews]
        
            return JsonResponse({'message' : 'SUCCESS', 'result' : result}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
        
        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)
        
    @login_decorator
    @transaction.atomic(using='default')
    def post(self, request, movie_id):
        try:
            review, created = Review.objects.update_or_create(
                user         = request.user,
                movie_id     = movie_id,
                defaults     = {
                    'title'        : request.POST.get('title'),
                    'content'      : request.POST.get('content'),
                    'rating'       : request.POST.get('rating'),
                    'watched_date' : request.POST.get('watched_date').split(' ')[0],
                    'watched_time' : request.POST.get('watched_date').split(' ')[1]
                }
            )
            
            file_handler = FileHander(s3_client)
            
            if not created :
                review_images_url = request.POST.get('review_images_url',[])
                review_images     = [review_image.image for review_image in ReviewImage.objects.filter(review_id=review.id)]
                
                for review_image in review_images:
                    if AWS_S3_URL+review_image.image_url in review_images_url:
                        continue
                    else:
                        file_handler.delete(review_image.image_url)
                        review_image.delete()
            
            review_images = request.FILES.getlist('review_images')
            
            for review_image in review_images:
                
                file_name = file_handler.upload(review_image,'image/review')
                image     = Image.objects.create(image_url=file_name)
                
                ReviewImage.objects.create(
                    image  = image,
                    review = review,
                )
                
            tags = request.POST.get('tags')
            
            if tags not in [None, '']:
                for tag_name in tags.split(','):
                    tag = Tag.objects.get_or_create(name=tag_name.strip())
                    ReviewTag.objects.create(
                        review = review,
                        tag    = tag[0]
                    )
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
                
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

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

            return JsonResponse({'message' : 'NO_CONTENTS'}, status=204)
        
        except Review.DoesNotExist:
            return JsonResponse({'message' : 'REVIEW_NOT_EXIST'}, status=400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)

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
