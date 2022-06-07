from django.urls import path
from users.views import KakaoLogIn, DeleteAccountView, KakaoLogInCallbackView, UserInformationView, UserProfileUpdateView
from users.views import LoginNaverCallBackView, LoginNaverView 

urlpatterns = [
    #카카오로그인
    path('login/kakao/token', KakaoLogIn.as_view()), #! 테스트용
    path('login/kakao/callback', KakaoLogInCallbackView.as_view()),
    
    #네이버로그인
    path('login/naver', LoginNaverView.as_view()),
    path('login/naver/callback', LoginNaverCallBackView.as_view()),
    
    #user_information
    path('info', UserInformationView.as_view()),
    
    #user_profile_update
    path('profile-update', UserProfileUpdateView.as_view()),
    
    #user_delete_account
    path('delete-account/<int:user_id>', DeleteAccountView.as_view()),
]