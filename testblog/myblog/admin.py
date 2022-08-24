from django.contrib import admin
from .models import Category, Topic


class TopicAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'time_created', 'time_updated', 'category', 'photo', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'category', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Topic, TopicAdmin)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # Automatic url in admin panel


admin.site.register(Category, CategoryAdmin)
