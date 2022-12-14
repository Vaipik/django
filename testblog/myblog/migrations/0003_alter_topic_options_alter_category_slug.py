# Generated by Django 4.1 on 2022-08-26 09:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_alter_topic_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-time_updated', '-time_created', 'category'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=100, populate_from='name', unique=True, verbose_name='URL'),
        ),
    ]
