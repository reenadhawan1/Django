from django.shortcuts import render, HttpResponse, redirect

def index(req):
    context = {
    "email" : "blog@gmail.com",
    "name" : "mike"
    }
    return render(req, "blogs_app/index.html", context)

def new(req):
    res = "placeholder to display a new form to create a new blog"
    return HttpResponse(res)

def create(req):
    if req.method == "POST":
        print("*"*50)
        print(req.POST)
        print(req.POST['name'])
        print(req.POST['desc'])
        req.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(req, number):
    res = 'placeholder to display blog ' + number
    return HttpResponse(res)

def edit(req, number):
    res = 'placeholder to display blog ' + number
    return HttpResponse(res)

def destroy(req, number):
    return redirect('/')