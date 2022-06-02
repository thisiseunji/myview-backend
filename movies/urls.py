from django.urls  import path
from movies.views import MovieDetailView, MovieTitleView

urlpatterns = [
    path('<int:movie_id>', MovieDetailView.as_view()),
    
    #영화 제목 검색 데이터
    path('titles', MovieTitleView.as_view())
]