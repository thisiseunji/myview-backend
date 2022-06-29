from django.urls  import path
from reviews.views import ReviewListView, ReviewView

urlpatterns = [
    #list
    path('', ReviewListView.as_view()),
    #create
    path('/movie/<int:movie_id>', ReviewView.as_view()),
    #read, delete
    path('/<int:review_id>', ReviewView.as_view()),
]