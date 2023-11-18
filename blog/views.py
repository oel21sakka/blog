from rest_framework import generics
from .models import Post
from .serializers import PostsSerializer

class PostsView (generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostsSerializer
    
class SinglePostView (generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostsSerializer