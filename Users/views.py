from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.


def signup(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name', 'default value')
        second_name = request.POST.get('second_name', 'default value')
        username = request.POST.get("username")
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).first():
                messages.info(request, 'username already taken')
                return redirect('signup')
            else:

                u = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=second_name)

                u.save()
                print('hello')
                return redirect('login')
        else:
            messages.info(request, 'please Enter Same Password')
            return redirect('signup')
    else:
        return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Details !!!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
