from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ['id']
        extra_kwargs = {
            'post': {'write_only': True},
        }

class PostsSerializer(serializers.ModelSerializer):
    
    comments = CommentSerializer(many = True, read_only = True)
    author = serializers.SlugRelatedField(read_only = True, slug_field='username')
    
    class Meta:
        model = Post
        fields = ['title','slug','body', 'author', 'publish', 'created', 'updated', 'status', 'comments']
        
        
class SharePostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255, required = True)
    recipient_email = serializers.EmailField(required = True)
    comments = serializers.CharField(max_length = 255, required = False, default= '')
    post = serializers.PrimaryKeyRelatedField(queryset = Post.objects.all(), required = True)
    
    