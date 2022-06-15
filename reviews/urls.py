from django.urls  import path
from views import ReviewView

urlpatterns = [
    #read
    path('', ReviewView.as_view()),
    #create or update
    path('<int:movie_id>', ReviewView.as_view()),
    #delete
    path('<int:review_id>', ReviewView.as_view()),
]