from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['repeat-pass']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save();
                print("User Created")
                return redirect('signIn')


        else:
            messages.info(request ,'Passwords dont match')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')


def signIn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Are you sure that is correct? Please try again!')
            return redirect('signIn')

    else:
        return render(request, 'signIn.html')

def signOut(request):
    auth.logout(request)
    return redirect('home')
