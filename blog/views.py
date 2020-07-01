from django import shortcuts
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return shortcuts.render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = shortcuts.get_object_or_404(Post, pk=pk)
    return shortcuts.render(request, 'blog/post_detail.html', {'post': post})
