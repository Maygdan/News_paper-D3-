from django.urls import path
from .views import *


urlpatterns = [
   path('', PostView.as_view(),name='posts_list'), 
   path('<int:pk>', PostDetail.as_view(),name='post'),
   path('news/create/',PostCreate.as_view(),name='news_create'),
   path('article/create/',PostCreate.as_view(),name='article_create'),
   path('news/<int:pk>/update/',PostUpdate.as_view(),name='news_update'),
   path('article/<int:pk>/update/',PostUpdate.as_view(),name='article_update'),
   path('news/<int:pk>/delete/',PostDelete.as_view(),name='news_delete'),
   path('article/<int:pk>/delete/',PostUpdate.as_view(),name='article_update'),
]