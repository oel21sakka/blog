from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone

class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    objects = models.Manager()
    published = PublishedPostsManager()
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish  = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
