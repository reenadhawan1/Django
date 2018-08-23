from django.shortcuts import render,redirect
from time import time, strftime

def index(req):
    return render(req,'user_login/index.html')