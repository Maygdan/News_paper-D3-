from django.views.generic import (ListView, DetailView,
CreateView,UpdateView,DeleteView)
from .forms import PostForm
from .models import Post
from datetime import datetime as dt
from django.urls import reverse_lazy
from .filters import PostFilter, CategoryFilter

class PostView(ListView):
    model=Post
    ordering='title'
    template_name='posts.html'
    context_object_name='posts'
    paginate_by=2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class PostDetail(DetailView):
    model=Post
    template_name='post.html'
    context_object_name='post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = dt.utcnow()
        return context
    
class PostCreate(CreateView):
    form_class=PostForm
    model=Post
    template_name='post_update.html'

class PostUpdate(UpdateView):
    form_class=PostForm
    model=Post
    template_name='post_update.html'

class PostDelete(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('posts_list')

class ArticletView(ListView):
    model=Post
    ordering='title'
    template_name='articles.html'
    context_object_name='articles'
    paginate_by=2
    













    