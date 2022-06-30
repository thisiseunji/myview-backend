from django.urls  import path
from reviews.views import ReviewListView, ReviewView

urlpatterns = [
    #list
    path('/list', ReviewListView.as_view()),
    #create, update
    path('', ReviewView.as_view()),
    #read, delete
    path('/<int:review_id>', ReviewView.as_view()),
]