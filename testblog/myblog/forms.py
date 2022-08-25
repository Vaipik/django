from django import forms
from django.core.exceptions import ValidationError

from .models import *


class NewTopicForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'No category selected'

    class Meta:

        model = Topic
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'for   m-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):  # validation for title

        title = self.cleaned_data['title']

        if len(title) > 200:
            raise ValidationError('Length is more than 200 symbols')

        return title
