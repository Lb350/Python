from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsEdit, NewsCreate, ArticlesCreate, ArticlesEdit, PostDelete

urlpatterns = [
    path('', PostList.as_view()),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('articles/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view()),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),

]