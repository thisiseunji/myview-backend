from django.urls  import path
from reviews.views import ReviewListView, ReviewView

urlpatterns = [
    #list
    path('/list', ReviewListView.as_view()),
    #create, update
    path('', ReviewView.as_view()),
    #read, delete
    #movie 상세페이지에서 호출할 수 있도록 movie_id를 이용한 호출 필요
    path('/<int:review_id>', ReviewView.as_view()),
]