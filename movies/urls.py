from django.urls  import path
from movies.views import MovieDetailView, MovieTitleView

urlpatterns = [
    # 영화 상세페이지
    path('detail/<int:movie_id>', MovieDetailView.as_view()),
    
    #영화 제목 검색 데이터
    path('titles', MovieTitleView.as_view()),
]