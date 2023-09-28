from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import OtherText
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages 
from .models import Profile
from .form import SignUpForm

def home_page(request):
    text = OtherText.objects.all()
    return render(request, 'article.html', {'text':text})


def logout_user(request):
    logout(request)
    messages1 = messages.success(request, 'Вы вышли из системы')
    return redirect('home_page')


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Неверное имя пользователя или пароль.')
            return redirect('/login_user')
    else:   
        return render(request, 'login.html', {})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #Получаем имя пользователя и пароль из формы
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})