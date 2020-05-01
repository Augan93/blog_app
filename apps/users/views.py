from django.shortcuts import render, redirect, HttpResponseRedirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def my_login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(
                request,
                username=cd['login'],
                password=cd['password']
            )
            if user and user.is_active:
                login(request, user)
                next = request.GET.get('next')
                if next:
                    return HttpResponseRedirect(redirect_to=next)
                return redirect('posts:posts')
            else:
                messages.error(request,
                               'Неверный пароль или логин')
    else:
        login_form = forms.LoginForm()

    return render(
        request,
        'users/login.html',
        {'login_form': login_form}
    )


@login_required
def my_logout(request):
    logout(request)
    return redirect('users:login')
