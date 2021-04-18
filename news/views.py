from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'