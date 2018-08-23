from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request,'book_reviews/index.html')

def register(request):
    errors = User.objects.registerValidator(request.POST)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        return redirect('/')
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(name =request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = pwHash)
    request.session['name'] = request.POST['name']
    request.session['id'] = user.id
    return redirect('/books/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        print(errors)
        return redirect('/')
    user = User.objects.get(email = request.POST['login_email'])
    request.session['name'] = user.name
    request.session['id'] = user.id
    return redirect('/books/')

def logout(request):
    request.session.flush()
    return redirect('/')

def books(request):
    content = {
        'reviews': Review.objects.all().order_by('-created_at')[:3],
        'books': Book.objects.all()
    }
    return render(request,'book_reviews/books.html',content)

def booksAdd(request):
    content = {
        'books': Book.objects.all()
    }
    return render(request,'book_reviews/add_book.html',content)

def addBook(request):
    user = User.objects.get(id=request.session['id'])
    if len(request.POST['new_author']) > 1:
        book = Book.objects.create(name = request.POST['name'],author = request.POST['new_author'])
    else:
        book = Book.objects.create(name = request.POST['name'],author = request.POST['author'])
    Review.objects.create(user = user,book = book, review = request.POST['review'], rating = request.POST['rating'])
    return redirect(f'/books/{book.id}')

def book(request,id):
    book = Book.objects.get(id=id)
    content = {
        'reviews': book.book_reviews.all(),
        "book" : book
    }
    return render(request,'book_reviews/book.html',content)