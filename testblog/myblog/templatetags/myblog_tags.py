from django import template
from django.db.models import Count

from myblog.models import *


register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    return Category.objects.all() if filter is None else Category.objects.filter(pk=filter)


@register.inclusion_tag('myblog/list_categories.html')
def publication(sort=None, cat_selected=0):
    categories = Category.objects.annotate(Count('topic')) if sort is None else Category.objects.order_by(sort)
    return {
        'categories': categories,
        'cat_selected': cat_selected,
    }

