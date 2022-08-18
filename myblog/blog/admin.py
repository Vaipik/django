from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'author', 'published_date')
    list_display_links = ('title', 'content', 'author')
    search_fields = ('title', 'author')


admin.site.register(Post, PostAdmin)


class CommentsAdmin(admin.ModelAdmin):

    list_display = ('post', 'text', 'author', 'published_date')
    list_display_links = ('post', 'text')
    search_fields = ('post', 'author')


admin.site.register(Comments, CommentsAdmin)
