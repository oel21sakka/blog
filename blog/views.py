from django.shortcuts import get_object_or_404
from email_config import EMAIL_HOST_USER
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from .models import Post,Comment
from .serializers import PostsSerializer, CommentSerializer, SharePostSerializer
from django.db.models import Count

class PostsView (generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostsSerializer

    
@api_view(['GET'])
def SinglePostView (request,year,month,day,post_slug):
    post = get_object_or_404(Post.published, slug = post_slug, publish__year = year, publish__month = month, publish__day = day)
    serializer = PostsSerializer(post)
    
    #get comments for the post
    comments = Comment.objects.all().filter(post = post.id)
    comments_serializer = CommentSerializer(comments,many = True)
    
    #get similar posts
    similar_posts = Post.published.filter(tags__in=post.tags.all()).exclude(id=post.id)
    #sort similar posts
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:3]
    similar_posts_serializer = PostsSerializer(similar_posts,many = True)
    
    response = serializer.data
    #add comments
    response['comments'] = comments_serializer.data
    #add similar posts to response
    response['similar_posts'] = similar_posts_serializer.data
    return Response(response)
    
class CommentView (generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
@api_view(['POST'])
def sharePostView(request):
    
    serializer = SharePostSerializer(data = request.data)
    
    if serializer.is_valid():
        post = Post.published.get(id=serializer.data['post'])
        post_url = f'{post.get_absolute_url()}/'
        subject = f"{serializer.data['name']} recommends you read {post.title}"
        message = f"Read {post.title} at {post_url}\n\n{serializer.data['name']}\'s comments: {serializer.data['comments']}"
        send_mail(subject, message, EMAIL_HOST_USER, [serializer.data['recipient_email']], )
        return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
