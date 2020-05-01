from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from uuid import uuid4
from blog.settings import BASE_DIR
import os

from . import models
from . import forms


def show_posts(request):
    """Получать постов"""
    latest_post = models.Post.objects.filter(is_active=True).latest('created')
    posts = models.Post.objects.filter(is_active=True).order_by('-created')[1:10]
    context = {
        'posts': posts,
        'latest_post': latest_post,
    }

    return render(request,
                  'posts/posts.html',
                  context=context)


@login_required
def create_post(request):
    """Создать пост"""
    form = forms.PostCreateForm()

    if request.method == 'POST':
        form = forms.PostCreateForm(data=request.POST,
                                    files=request.FILES)
        if form.is_valid():
            form.save(context={'request': request})
            messages.success(request, 'Success!')

    context = {
        'form': form
    }

    return render(
        request,
        'posts/new_post.html',
        context=context
    )


def initialize_data(request):
    data = [
        {
            'title': 'Почему подросткам стоит изучать программирование?',
            'text': 'Объясняем почему словосочетание «программирование для подростков» не должно вызывать скептическую улыбку и какие полезные навыки приобретают ребята, изучая программирование.',
        },
        {
            'title': 'Here we will show you how to create some commonly used',
            'text': 'Here we will show you how to create some commonly used layouts with our grid system. Hopefully these will get you more comfortable with laying out elements. To keep these demos simple, the ones here will not be responsive.',
        },
        {
            'title': 'Here we will show you how to create some commonly used',
            'text': 'Here we will show you how to create some commonly used layouts with our grid system. Hopefully these will get you more comfortable with laying out elements. To keep these demos simple, the ones here will not be responsive.',
        },
        {
            'title': 'Dividers are 1 pixel lines that help',
            'text': 'Dividers are 1 pixel lines that help break up your content. Just add the divider to a div in between your content.'
        },
        {
            'title': 'Here we will show you how to create some commonly used',
            'text': 'Here we will show you how to create some commonly used layouts with our grid system. Hopefully these will get you more comfortable with laying out elements. To keep these demos simple, the ones here will not be responsive.',
        },
        {
            'title': 'Here we will show you how to create some commonly used',
            'text': 'Here we will show you how to create some commonly used layouts with our grid system. Hopefully these will get you more comfortable with laying out elements. To keep these demos simple, the ones here will not be responsive.',
        },
        {
            'title': 'Почему подросткам стоит изучать программирование?',
            'text': 'Объясняем почему словосочетание «программирование для подростков» не должно вызывать скептическую улыбку и какие полезные навыки приобретают ребята, изучая программирование.',
        },
        {
            'title': 'Почему подросткам стоит изучать программирование?',
            'text': 'Объясняем почему словосочетание «программирование для подростков» не должно вызывать скептическую улыбку и какие полезные навыки приобретают ребята, изучая программирование.',
        },

    ]

    for post in data:
        u, _ = User.objects.get_or_create(username='author',
                                          email='author@mail.ru')
        u.set_password('123')
        u.save()

        post = models.Post(**post,
                           author=u)

        image_path = os.path.join(BASE_DIR, 'static/images/image.png')
        with open(image_path, 'rb') as f:
            image = f.read()

        image_name = '{}.png'.format(str(uuid4()))
        post.image.save(image_name,
                        ContentFile(image),
                        save=False)
        post.save()

    return HttpResponse('ok')
