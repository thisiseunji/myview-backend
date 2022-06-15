from random        import randrange
from django.http   import JsonResponse
from django.views  import View

from core.utils     import login_decorator
from core.storages  import FileHander, s3_client
from movies.models  import Movie, Image
from reviews.models import ColorCode, ReviewImage, Tag, Review, ReviewTag
from my_settings    import AWS_S3_URL

class ReviewView(View):
    @login_decorator
    def get(self, request):
        try:
            user    = request.user
            reviews = Review.objects.all(user=user)
            result  = [
                { 
                    'review_id'     : review.id,
                    'title'         : review.title,
                    'content'       : review.content,
                    'rating'        : review.rating,
                    'watched_date'  : review.watched_date,
                    'watched_time'  : review.watched_time,
                    'review_images' : [AWS_S3_URL+review_image.image.image_url for review_image in ReviewImage.objects.filter(review=review)],
                    #값이 없을 경우 리턴 값
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
    def post(self, request, movie_id):
        try:
            review = Review.objects.update_or_create(
                user         = request.user,
                movie        = Movie.objects.get(id=movie_id),
                defaults     = {
                    'user'         : request.user,
                    'movie'        : Movie.objects.get(id=movie_id),
                    'title'        : request.POST('title'),
                    'content'      : request.POST('content'),
                    'rating'       : request.POST('rating'),
                    #가공 0000-00-00 00:00:00
                    'watched_date' : request.POST('watched_date').split(' ')[0],
                    'watched_time' : request.POST('watched_time').split(' ')[1],
                }
            )
            
            #리뷰 이미지 업로드, 업데이트           
            file_hander = FileHander(s3_client)
            
            review_images = request.FILES.getlist('review_images')
            
            for review_image in review_images:
                
                file_name = file_hander.upload(review_image, 'image/review/')
                image     = Image.objects.get_or_create(image_url=file_name)
                
                ReviewImage.objects.update_or_create(
                    image  = image,
                    review = review,
                    defaults= {
                        'image'  : image,
                        'review' : review
                    }
                )
            
            if request.POST['tags'].exist():
                [Tag.objects.update_or_create(name=tag, defaults={'name':tag}) for tag in request.POST['tags']]
            
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
            
            review.delete()

            return JsonResponse({'message' : 'NO_CONTENTS'}, status=204)
        
        except Review.DoesNotExist:
            return JsonResponse({'message' : 'REVIEW_NOT_EXIST'}, status=400)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

        except ValueError:
            return JsonResponse({'message' : 'VALUE_ERROR'}, status=400)