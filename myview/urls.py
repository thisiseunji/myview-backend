from django.urls import include, path

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('user', include('users.urls')),
    path('movie', include('movies.urls')),
    path('review', include('reviews.urls')),
    path('admin', include('adminpage.urls'))
]
