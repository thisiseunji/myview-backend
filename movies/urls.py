from django.urls  import path

from movies.views import MovieDetailView, MovieReviewView, SimpleSearchView, MovieSearchView, ActorDetailView,\
                         ActorListView, ActorIntimacyView, MovieListView
                         
urlpatterns = [
    # 영화 상세페이지
    path('/detail/<int:movie_id>', MovieDetailView.as_view()),
    
    #영화 리뷰 전체
    path('/<int:movie_id>/reviews', MovieReviewView.as_view()),
    
    #영화 검색 데이터
    #path('/simple', SimpleSearchView.as_view()),
    path('/simple', SimpleSearchView.as_view()),
    
    #영화 검색
    #path('', MovieSearchView.as_view()),
    path('', MovieSearchView.as_view()),
    
    # 영화배우 상세페이지
    path('/actor/<int:actor_id>', ActorDetailView.as_view()),
    path('/actor', ActorDetailView.as_view()),
    
    # 영화배우 리스트
    path('/actor/list', ActorListView.as_view()),
    
    # 영화배우 친밀도
    path('/actor/intimacy/<int:actor_id>', ActorIntimacyView.as_view()),
    
    # [관리자] 전체 영화데이터 리스트
    path('/all', MovieListView.as_view()),
]