import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from .models import Post

class LatestBlogPostsFeed(Feed):
    title = "Blog Posts Feed"
    link = "/feed/"
    description = "get latest posts"

    def items(self):
        return Post.objects.order_by("-publish")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)