from django.urls import path

from users.views import NaverLoginCallbackView, NaverLoginView

urlpatterns = [
    path('naver/login', NaverLoginView.as_view()),
    path('naver/login/callback', NaverLoginCallbackView.as_view()),
]
