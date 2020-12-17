from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
# Create your views here.
@unauthenticated_user
def register(request):
    nav = 'bg-dark'
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created ' + user)
            return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form, 'nav': nav})

@unauthenticated_user
def loginPage(request):
    nav = 'bg-dark'

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, "registration/login.html",{'nav': nav})