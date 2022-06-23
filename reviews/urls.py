from django.urls  import path
from reviews.views import ReviewListView, ReviewView

urlpatterns = [
    #list
    path('', ReviewListView.as_view()),
    #read
    path('<int:review_id>', ReviewView.as_view()),
    #create #업데이트는 어떻게 할 것인지
    path('movies/<int:movie_id>', ReviewView.as_view()),
    #delete
    path('<int:review_id>', ReviewView.as_view()), 
]