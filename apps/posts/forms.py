from django import forms
from django_summernote.widgets import SummernoteWidget
from . import models


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            'title',
            'text',
            'image',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название статьи',
                }
            ),
            'text': SummernoteWidget(),
            'image': forms.FileInput(
                attrs={
                    'onchange': 'loadFile(event)',
                    'id': 'imageId',
                }
            )
        }

    def save(self, commit=False, context=None):
        post = super().save(commit=commit)
        post.author = context['request'].user
        post.save()

        return post
