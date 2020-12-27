from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post


def home(request):

    all_posts = Post.objects.all()
    return render(request, 'task1/index.html', {'posts': all_posts})

def post_single(request,post):
    post = get_object_or_404(Post, slug=post)
    return render(request, 'task1/detail.html', {'post': post})
