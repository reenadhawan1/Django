from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

def index(req):
    if 'name' in req.session:
        req.session['name'] += 1
    else:
        req.session['name'] = 1
    content = {
        'rand': get_random_string(length=14),
    }
    if 'name' in req.session:
        print(req.session['name'])
    return render(req,'randWordAPP/index.html', content)

def reset(req):
    if 'name' in req.session:
        req.session.pop('name')
    return redirect('/random_word')
