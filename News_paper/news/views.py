from django.views.generic import (ListView, DetailView,
CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import PostForm
from .models import Post
from datetime import datetime as dt
from django.urls import reverse_lazy
from .filters import PostFilter

class AllView(ListView):
    model=Post
    ordering='title'
    template_name='posts.html'
    context_object_name='posts'
    paginate_by=10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
class PostsUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'posts_edit.html'
    
class NewsCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_new',)
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        a = form.save(commit=False)
        a.choose = 'news'
        return super().form_valid(form)

class ArticleCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('news.add_article',)
    form_class = PostForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        a = form.save(commit=False)
        a.choose = 'article'
        return super().form_valid(form)
    


class PostsDelete(PermissionRequiredMixin,DeleteView):
    permission_required = ('news.delete_post',)
    model=Post
    template_name='posts_delete.html'
    success_url=reverse_lazy('posts_list')

    
class PostsDetail(PermissionRequiredMixin,DetailView):
    model=Post
    template_name='post.html'
    context_object_name='post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = dt.utcnow()
        return context
    
















    