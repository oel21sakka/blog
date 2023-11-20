from django.urls import path
from .views  import PostsView, SinglePostView, CommentView, sharePostView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:post_id>/', SinglePostView),
    path('comment', CommentView.as_view()),
    path('share', sharePostView),
]
