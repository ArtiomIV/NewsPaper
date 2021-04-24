from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
from django.views.generic.detail import DetailView
from .models import Post
from .filters import PostFilter
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by =  10

class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by =  1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'