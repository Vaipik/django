from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Topic


def index(request):

    topics = Topic.objects.all()

    context = {
        'topics': topics,
        'title': 'Main page',
    }

    return render(request, 'myblog/index.html', context)


def about(request):

    context = {
        'title': 'About',
    }

    return render(request, 'myblog/about.html', context)


def category(request, cat_slug):

    topics = Topic.objects.filter(category__slug=cat_slug)

    if len(topics) == 0:
        raise Http404()

    context = {
        'topics': topics,
        'title': f'{topics[0].category.name} category',
        'cat_selected': cat_slug,
    }

    return render(request, 'myblog/index.html', context)


def feedback(request):
    pass


def login(request):
    pass


def publication(request, pub_slug, cat_slug):

    post = get_object_or_404(Topic, slug=pub_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.category.slug,
    }

    return render(request, 'myblog/publication.html', context)


def new_topic(request):
    pass


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page does not exist</h1></p>{exception}</p>')
