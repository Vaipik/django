from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('new_topic/', new_topic, name='new_topic'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('category/<slug:cat_slug>', category, name='category'),
    path('<slug:cat_slug>/<slug:pub_slug>', publication, name='publication'),
]

