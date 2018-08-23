from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    content = {
        'users': User.objects.all()
    }
    return render(request,'users/index.html',content)

def new(request):
    return render(request,'users/new.html')

def edit(request,id):
    return render(request,'users/edit.html',{ 'user': User.objects.get(id=id)})

def show(request, id):
    return render(request,'users/show.html',{ 'user': User.objects.get(id=id)})

def create(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/users')

def destroy(request,id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def update(request,id):
    this_user = User.objects.get(id=id)
    this_user.first_name = request.POST['first_name']
    this_user.last_name = request.POST['last_name']
    this_user.email = request.POST['email']
    this_user.save()
    return redirect('/users')