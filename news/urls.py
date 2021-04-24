from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('search/', PostSearch.as_view()),
    path('<int:pk>', PostDetail.as_view())
]