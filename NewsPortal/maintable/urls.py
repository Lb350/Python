from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsEdit, NewsCreate, ArticlesCreate, ArticlesEdit, NewsDelete, ArticlesDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('articles/<int:pk>/edit/', ArticlesEdit.as_view(), name='articles_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='articles_delete'),

]
