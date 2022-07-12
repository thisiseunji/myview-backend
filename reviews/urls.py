from django.urls  import path
from reviews.views import ReviewListView, ReviewView, ReviewTopThreeView

urlpatterns = [
    #list
    path('/list', ReviewListView.as_view()),
    #create, update
    path('', ReviewView.as_view()),
    #read
    path('/movie/<int:movie_id>', ReviewView.as_view()),
    #delete
    path('/<int:review_id>', ReviewView.as_view()),
    #top3
    path('/top3', ReviewTopThreeView.as_view()),
]