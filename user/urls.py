from django.urls import path, re_path
from user import views as user_views


urlpatterns = [

    re_path('anime_content', user_views.TopAnimeViewSet.as_view({'post': 'create', 'get':'list'})),
]
