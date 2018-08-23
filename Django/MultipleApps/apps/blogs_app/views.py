from django.shortcuts import render, HttpResponse, redirect

def index(req):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(req):
    res = "placeholder to display a new form to create a new blog"
    return HttpResponse(res)

def create(req):
    return redirect("/blogs")

def show(req, number):
    res = 'placeholder to display blog ' + number
    return HttpResponse(res)

def edit(req, number):
    res = 'placeholder to display blog ' + number
    return HttpResponse(res)

def destroy(req, number):
    return redirect('/blogs')