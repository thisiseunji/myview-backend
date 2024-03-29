from django.urls  import path

from movies.views import MovieDetailView, MovieReviewView, MoviePopularView, MovieLatestView, MovieSearchView, ActorDetailView, ActorSearchView

urlpatterns = [
    # 영화 상세페이지
    path('/detail', MovieDetailView.as_view()),
    
    #영화 리뷰 전체
    path('/<int:movie_id>/reviews', MovieReviewView.as_view()),
    
    #영화 검색 추천 데이터
    path('/popular', MoviePopularView.as_view()),
    
    #최신영화
    path('/latest', MovieLatestView.as_view()),

    #영화 검색
    path('', MovieSearchView.as_view()),
    
    #배우 검색
    path('/actor', ActorSearchView.as_view()),
    
    # 영화배우 상세페이지
    path('/actor/detail', ActorDetailView.as_view()),
    
    # # 영화배우 리스트
    # path('/actor/list', ActorListView.as_view()),
    
    # # 영화배우 친밀도
    # path('/actor/intimacy/<int:actor_id>', ActorIntimacyView.as_view()),
    
    # # [관리자] 전체 영화데이터 리스트
    # path('/all', MovieListView.as_view()),
    
    # # [관리자] 영화배우 데이터 생성
    # path('/actor/create', ActorDetailView.as_view()),

]