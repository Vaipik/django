from django.db.models import Count

from .models import *


class DataMixin:

    paginate_by = 3

    def get_user_context(self, **kwargs):

        context = kwargs
        categories = Category.objects.annotate(Count('topic'))
        context['categories'] = categories

        user_menu = menu.copy()
        if self.request.user.is_authenticated:
            user_menu.insert(len(user_menu) - 2, {'title': "New publication", 'url_name': 'new_topic'},)
            # len(user_menu) - 2 -> to keep log in last item in list
        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context


menu = [
        {'title': "Home", 'url_name': 'home'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Feedback", 'url_name': 'feedback'},
        {'title': "Log in", 'url_name': 'login'},
    ]
