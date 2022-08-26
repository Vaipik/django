from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewTopicForm, RegisterUserForm, LoginUserForm
from .models import Topic
from .utils import *


class BlogHomePage(DataMixin, ListView):

    model = Topic
    template_name = 'myblog/index.html'
    context_object_name = 'topics'  # tag in templates and further access
    # extra_context = {'title': 'Main page'}  # Only for immutable data

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Home page'))

        return context


def about(request):
    context = {
        'title': 'About',
    }

    return render(request, 'myblog/about.html', context)


class TopicCategory(DataMixin, ListView):

    model = Topic
    template_name = 'myblog/index.html'
    context_object_name = 'topics'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title=context.get('topics')[0].category.name + ' category',
                                             cat_selected=context.get('topics')[0].category.slug))

        return context

    def get_queryset(self):
        return Topic.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


def feedback(request):
    pass


class ShowPublication(DataMixin, DetailView):

    model = Topic
    template_name = 'myblog/publication.html'
    slug_url_kwarg = 'pub_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title=context['post'],
                                             cat_selected=context['post'].category.slug))

        return context


class NewTopic(LoginRequiredMixin, DataMixin, CreateView):

    form_class = NewTopicForm
    template_name = 'myblog/new_topic.html'
    # success_url = reverse_lazy() if no get_absolute_url determined in Model
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='New publication'))

        return context


class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'myblog/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Registration'))

        return context

    def form_valid(self, form):

        user = form.save()
        login(self.request, user)

        return redirect('home')

    def get_success_url(self):
        return reverse_lazy('home')


class LoginUser(DataMixin, LoginView):

    form_class = LoginUserForm
    template_name = 'myblog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Login page'))

        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Page does not exist</h1></p>{exception}</p>')


