from rest_framework import generics
from .models import Post,Comment
from .serializers import PostsSerializer, CommentSerializer

class PostsView (generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostsSerializer
    
class SinglePostView (generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostsSerializer
    
class CommentView (generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer