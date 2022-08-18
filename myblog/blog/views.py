from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import *
from .forms import *


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


class PostCreateView(CreateView):

    template_name = 'blog/new_publication.html'
    form_class = PostForm
    success_url = reverse_lazy('index')
