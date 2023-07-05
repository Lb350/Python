from django.urls import path
from .views import PostList, PostDetail,PostSearch, PostEdit, PostCreate, PostDelete

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('news/search/', PostSearch.as_view())
]