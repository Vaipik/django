from django.shortcuts import render
from .models import *


def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def topic(request, topic_id):

    current_post = Post.objects.get(pk=topic_id)
    comments = Comments.objects.filter(post=topic_id)


    context = {
        'post': current_post,
        'comments': comments,
    }

    return render(request, 'blog/by_publication.html', context)

