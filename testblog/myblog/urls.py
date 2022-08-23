from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('new_topic/', new_topic, name='new_topic'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('publication/<int:pub_id>', publication, name='publication'),
    path('category/<int:cat_id>', category, name='category'),
]

