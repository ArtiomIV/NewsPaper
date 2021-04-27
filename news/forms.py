from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Post

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['titile_state', 'post_title', 'post_text', 'author', 'category']