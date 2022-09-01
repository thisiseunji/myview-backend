from django.urls  import path

from movies.views import MovieDetailView, MovieReviewView, MoviePopularView, MovieSearchView

urlpatterns = [
    # 영화 상세페이지
    path('/detail/<int:movie_id>', MovieDetailView.as_view()),
    
    #영화 리뷰 전체
    path('/<int:movie_id>/reviews', MovieReviewView.as_view()),
    
    #영화 검색 추천 데이터
    path('/popular', MoviePopularView.as_view()),
    
    #영화 검색
    path('', MovieSearchView.as_view()),   
]