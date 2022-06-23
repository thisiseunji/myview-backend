from django.urls  import path
from movies.views import MovieDetailView, SimpleSearchView, ActorDetailView, ActorListView

urlpatterns = [
    # 영화 상세페이지
    path('/detail/<int:movie_id>', MovieDetailView.as_view()),
    
    #영화 검색 데이터
    path('/simple', SimpleSearchView.as_view()),
    
    # 영화배우 상세페이지
    path('/actor/<int:actor_id>', ActorDetailView.as_view()),
    path('/actor', ActorDetailView.as_view()),
    
    # 영화배우 리스트
    path('/actor', ActorListView.as_view()),
]