from django import template
from blog.models import Post,Comment

register = template.Library()
@register.inclusion_tag('blog/lastest_posts.html')
def lastest_posts ():
    
    context = {
        'l_posts' : Post.objects.all()[:7]

    }
    return context

@register.inclusion_tag('blog/lastest_comments.html')
def lastest_comments ():
    context = {
        'l_comments' : Comment.objects.filter(active=True)[:7],

    }
    return context

