from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('topics/<int:topic_id>', topic, name='post'),
    path('add/', PostCreateView.as_view(), name='add'),
]
