from django.urls import path
from blog.feeds import LatestBlogPostsFeed
from .views  import PostsView, SinglePostView, CommentView, sharePostView, searchView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', SinglePostView, name='post_detail'),
    path('comment', CommentView.as_view()),
    path('share', sharePostView),
    path('feed', LatestBlogPostsFeed()),
    path('search', searchView),
]
