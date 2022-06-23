from django.urls  import path
from reviews.views import ReviewView

urlpatterns = [
    #read
    path('', ReviewView.as_view()),
    #create
    path('/movies/<int:movie_id>', ReviewView.as_view()),
    #delete
    path('/<int:review_id>', ReviewView.as_view()),
]