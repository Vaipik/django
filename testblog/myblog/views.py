from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Topic, Category


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


def category(request, cat_id):

    topics = Topic.objects.filter(category_id=cat_id)

    if len(topics) == 0:
        raise Http404()

    context = {
        'topics': topics,
        'title': f"{topics[0].category.name} category",
    }

    return render(request, 'myblog/index.html', context)


def feedback(request):
    pass


def login(request):
    pass


def publication(request, pub_id):
    return HttpResponse(f"{pub_id}")


def new_topic(request):
    pass


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page does not exist</h1></p>{exception}</p>')
