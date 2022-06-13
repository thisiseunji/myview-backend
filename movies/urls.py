from django.urls  import path
from movies.views import MovieDataView, MovieDetailView, MovieTitleView, ActorDataView

urlpatterns = [
    # 영화 상세페이지
    path('detail/<int:movie_id>', MovieDetailView.as_view()),
    
    # 영화 정보 생성
    path('create', MovieDataView.as_view()),
    
    # 영화 정보 업데이트
    path('update', MovieDataView.as_view()),
    
    # 영화 정보 삭제
    path('delete', MovieDataView.as_view()),
    
    #영화 제목 검색 데이터
    path('titles', MovieTitleView.as_view()),
    
    # 배우 이름 조회
    path('actor/list', ActorDataView.as_view()),
    
    # 배우 생성
    path('actor/create', ActorDataView.as_view()),
    
    # 배우 정보 업데이트
    path('actor/update', ActorDataView.as_view()),
    
    # 배우 정보 삭제
    path('actor/delete', ActorDataView.as_view()),
]