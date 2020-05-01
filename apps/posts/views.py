from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import models
from . import forms


@login_required
def show_posts(request):
    return render(request,
                  'posts/posts.html')


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
