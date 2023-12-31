from rest_framework import serializers
from .models import Post,Comment
from taggit.serializers import TaggitSerializer,TagListSerializerField

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        exclude = ['id']
        extra_kwargs = {
            'post': {'write_only': True},
        }

class PostsSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(read_only = True, slug_field='username')
    tags = TagListSerializerField()
    post_link = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_post_link(self,obj):
        return obj.get_absolute_url()
        
        
class SharePostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255, required = True)
    recipient_email = serializers.EmailField(required = True)
    comments = serializers.CharField(max_length = 255, required = False, default= '')
    post = serializers.PrimaryKeyRelatedField(queryset = Post.objects.all(), required = True)
    
    
class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(max_length = 255, default = '')