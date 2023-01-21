from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.contrib.auth import authenticate,login,logout
import json

def home(request):
    global CONTAINER
    if request.user.is_anonymous:
        return redirect('home/index.html')

    if request.method == 'POST':

        return HttpResponse("")
    return render(request,'home/index.html') \
        
def my_books(request):
    return render(request,'home/my_books.html')        

def login(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(User.objects.values_list("password",))

        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')

        else:
            # No backend authenticated the credentials
            context= {'case':False}
            return render(request,'home/index.html',context)


    context= {'case':True}
    return render(request,'home/index_logined.html',context)

def logout_auth(request):
    logout(request)
    return redirect('home/index.html')

def signup(request):
    context= {'username':True,'email':True}
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')



        if (username,) in User.objects.values_list("username",) :
            context['username'] = False
            return render(request,'home/index_logined.html',context)

        elif (email,) in User.objects.values_list("email",):
            context['email'] = False
            return render(request,'home/index_logined.html',context)
        
        new_user = User.objects.create_user(username,email,password)
        new_user.save()
        login(request,new_user)
        return redirect('/')
    return render(request,'home/index_logined.html',context)