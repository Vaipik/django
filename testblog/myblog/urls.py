from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', BlogHomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('new_topic/', NewTopic.as_view(), name='new_topic'),
    path('feedback/', feedback, name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('category/<slug:cat_slug>', TopicCategory.as_view(), name='category'),
    path('<slug:cat_slug>/<slug:pub_slug>', ShowPublication.as_view(), name='publication'),
]

