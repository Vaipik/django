from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Post(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='Вміст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    published_date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публікації')

    class Meta:

        verbose_name_plural = 'Публікації'
        verbose_name = 'Публікація'
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class Comments(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Публікація')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user),
                               verbose_name='Автор коментаря')
    published_date = models.DateTimeField(auto_now_add=True, db_index=True,
                                          verbose_name='Дата публікації')

    class Meta:

        verbose_name_plural = 'Коментарі'
        verbose_name = 'Коментар'
        ordering = ['-published_date']
