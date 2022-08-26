from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class Topic(models.Model):

    title = models.CharField(max_length=255, verbose_name='Title')
    slug = AutoSlugField(max_length=100, populate_from='title', unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Text')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='photo')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    class Meta:

        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
        ordering = ['-time_updated', '-time_created', 'category']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pub_slug': self.slug, 'cat_slug': self.category.slug},)


class Category(models.Model):

    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = AutoSlugField(max_length=100, populate_from='name', unique=True, db_index=True, verbose_name='URL')

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
