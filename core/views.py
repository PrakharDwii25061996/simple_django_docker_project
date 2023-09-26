from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from .models import User


def index(request):
    return render(request, 'core/index.html', {})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'user_list': users})


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        User.objects.create_user(
            name=name,
            email=email,
            password=password,
            image=image
        )
        return redirect('user_list')
    return render(request, 'core/registration.html', {})


@login_required
def user_edit(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.mobile_number = request.POST.get('mobile')
        user.save()
        return redirect('user_list')
    return render(request, 'core/user_edit.html', {'user': user})


@login_required
def user_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('user_list')


def user_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('user_login')
    return render(request, 'core/user_login.html', {})


def user_logout(request):
    logout(request)
    return redirect('user_login')
