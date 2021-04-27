from django.core import paginator
from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView, DateDetailView, CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.views.generic.edit import DeleteView, UpdateView


from .filters import PostFilter
from .models import Post, Categories
from .forms import PostForm


# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by =  4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Categories.objects.all()
        context['form'] = PostForm()

        return context

class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-post_date')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetail(DetailView):
    template_name = 'post.html'
    queryset = Post.objects.all()

class PostCreateView(CreateView):
    template_name = 'create.html'
    form_class = PostForm

class PostUpdateView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk = id)

class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'