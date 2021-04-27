from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostSearch, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', PostList.as_view(), name = 'posts_list'),
    path('search/', PostSearch.as_view(), name = 'post_search'),
    path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
    path('create/', PostCreateView.as_view(), name = 'post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name = 'post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
]