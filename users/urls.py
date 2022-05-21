from django.urls import path

# from users.views import NaverLoginCallbackView, NaverLoginView, KakaoLoginIn
from users.views import KakaoLogInView,KakaoLogInCallbackView

urlpatterns = [
    # path('naver/login', NaverLoginView.as_view()),
    # path('naver/login/callback', NaverLoginCallbackView.as_view()),
    path('login/kakao', KakaoLogInView.as_view()),
    path('login/kakao/callback', KakaoLogInCallbackView.as_view()),
]
