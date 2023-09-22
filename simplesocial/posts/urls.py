from django.urls import path
from .views import PostDetail, PostList, UserPosts, CreatePost, DeletePost

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('new/', CreatePost.as_view(), name='create'),
    path('by/<username>/', UserPosts.as_view(), name='for_user'),
    path('by/<username>/<pk>/', PostDetail.as_view(), name='single'),
    path('delete/<pk>/', DeletePost.as_view(), name='delete'),
]
