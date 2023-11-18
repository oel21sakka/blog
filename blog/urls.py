from django.urls import path
from .views  import PostsView,SinglePostView

urlpatterns = [
    path('', PostsView.as_view()),
    path('<int:pk>/', SinglePostView.as_view())
]
