from django.urls import path
from .views import *


urlpatterns = [ 
   path('', AllView.as_view(),name='posts_list'), 
   path('<int:pk>', PostsDetail.as_view(),name='post_detail'),
   path('news/create/',NewsCreate.as_view(),name='news_create'),
   path('article/create/',ArticleCreate.as_view(),name='article_create'),
   path('<int:pk>/delete/',PostsDelete.as_view(),name='posts_delete'),
   path('<int:pk>/edit/',PostsUpdate.as_view(),name='post_edit'),
]